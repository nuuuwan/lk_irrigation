# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_19:00:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,475 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 19:00:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-13 19:00:57 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:00:44 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-13 19:00:22 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-06-13 19:00:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.53 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-06-13 18:03:20 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.011 |  |
| 2026-06-13 18:07:31 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-06-13 18:01:58 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-13 18:05:49 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 18:02:16 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 18:01:56 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 18:00:55 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-13 18:02:48 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:00:17 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:02:00 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:02:28 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:01:51 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:00:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:00:57 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:08:09 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:00:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 18:04:34 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-06-13 18:05:27 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-13 19:00:44 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-13 18:05:02 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.010 |  |
| 2026-06-13 18:05:32 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.011 |  |
| 2026-06-13 18:01:15 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | -0.012 |  |
| 2026-06-13 18:04:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-06-13 18:03:03 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-06-13 18:07:16 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | -0.021 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-13 18:03:52 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.021 |  |
| 2026-06-13 18:07:04 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.030 |  |
| 2026-06-13 18:02:56 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.031 |  |
| 2026-06-13 19:00:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-13 19:00:22 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 18:06:10 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.049 |  |
| 2026-06-13 18:04:24 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.051 |  |
| 2026-06-13 18:05:43 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.064 |  |
| 2026-06-13 18:03:29 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)