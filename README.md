# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_12:13:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 12:13:22 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -0.039 |  |
| 2026-06-13 12:11:10 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-13 12:09:47 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:09:40 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:09:34 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 12:09:27 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 12:07:37 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-06-13 12:07:27 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.189 |  |
| 2026-06-13 12:07:12 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:07:06 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:06:36 | Rathnapura (Kalu Ganga) | 5.44 | 🟡 Alert | -0.097 |  |
| 2026-06-13 12:06:17 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 12:05:41 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-13 12:05:37 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:05:36 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:05:20 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | -0.005 |  |
| 2026-06-13 12:04:06 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-06-13 12:03:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:03:50 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-13 12:03:44 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 12:03:42 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:03:34 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.000 |  |
| 2026-06-13 12:02:59 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:02:44 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.029 |  |
| 2026-06-13 12:02:41 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.041 |  |
| 2026-06-13 12:02:40 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.049 |  |
| 2026-06-13 12:02:33 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.47 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 12:02:22 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-13 12:02:19 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 12:02:12 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-06-13 12:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-13 12:01:44 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:01:36 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:01:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-13 12:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:00:57 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:00:46 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-06-13 12:00:13 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-13 11:51:54 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.115 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 12:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.47 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 12:03:34 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.000 |  |
| 2026-06-13 12:02:40 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.049 |  |
| 2026-06-13 12:06:36 | Rathnapura (Kalu Ganga) | 5.44 | 🟡 Alert | -0.097 |  |
| 2026-06-13 12:02:22 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-13 12:05:41 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-13 12:03:50 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-13 12:11:10 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-13 12:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-13 12:02:19 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 12:09:27 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 12:06:17 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 12:01:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-13 12:03:44 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 12:09:34 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 12:01:36 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:07:12 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:01:44 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:09:40 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:05:37 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:03:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:09:47 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 12:05:20 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | -0.005 |  |
| 2026-06-13 12:02:33 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:00:13 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:03:42 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:05:36 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:07:06 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:02:59 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-13 12:00:46 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-06-13 12:07:37 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-06-13 12:02:12 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-06-13 12:02:44 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.029 |  |
| 2026-06-13 12:04:06 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-06-13 12:13:22 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -0.039 |  |
| 2026-06-13 12:02:41 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.041 |  |
| 2026-06-13 12:07:27 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)