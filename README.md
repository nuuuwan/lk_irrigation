# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_21:11:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,882 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 21:07:32 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | -0.138 |  |
| 2026-06-29 21:01:59 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-29 21:04:04 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-29 21:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-29 21:02:37 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-29 21:04:10 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 21:02:47 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:03:07 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:05:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:00:57 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:01:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:05:20 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:09:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:06:56 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:01:43 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:03:41 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:05:58 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:07:19 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:05:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:04:16 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:04:22 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:01:53 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:05:52 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 21:02:44 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-06-29 21:01:57 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-29 21:04:33 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-06-29 21:02:04 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-29 21:08:43 | Kithulgala (Kelani Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-06-29 21:11:19 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.029 |  |
| 2026-06-29 21:03:54 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-06-29 21:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-06-29 21:10:19 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.049 |  |
| 2026-06-29 21:06:53 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.056 |  |
| 2026-06-29 21:07:49 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.096 |  |
| 2026-06-29 21:02:41 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)