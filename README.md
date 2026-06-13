# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_21:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 21:11:57 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.023 |  |
| 2026-06-13 21:11:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-06-13 21:08:37 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-06-13 21:07:38 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:07:36 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:06:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:06:50 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | -0.009 |  |
| 2026-06-13 21:06:03 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:05:58 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-06-13 21:05:38 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.037 |  |
| 2026-06-13 21:05:15 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 21:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-06-13 20:04:05 | Magura (Kalu Ganga) | 4.01 | 🟡 Alert | -0.020 |  |
| 2026-06-13 21:01:59 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 21:04:26 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 21:01:27 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 21:04:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 21:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 21:01:32 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 21:03:02 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:02:54 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:04:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:07:38 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:03:42 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:06:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:05:15 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:02:30 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:07:36 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:06:03 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:02:28 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:11:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-06-13 21:06:50 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | -0.009 |  |
| 2026-06-13 21:03:19 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-13 21:02:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-13 21:02:24 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-06-13 21:05:58 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-06-13 21:03:28 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.020 |  |
| 2026-06-13 21:04:24 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.020 |  |
| 2026-06-13 21:02:43 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-13 21:11:57 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.023 |  |
| 2026-06-13 21:08:37 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-06-13 21:03:34 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.031 |  |
| 2026-06-13 21:01:16 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.036 |  |
| 2026-06-13 21:05:38 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.037 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 21:03:17 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.050 |  |
| 2026-06-13 21:04:03 | Rathnapura (Kalu Ganga) | 4.78 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)