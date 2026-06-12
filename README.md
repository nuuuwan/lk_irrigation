# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_19:30:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,620 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 19:30:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.056 | 🔺 Rising |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:32 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:08 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:18:54 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-12 19:11:27 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:07:49 | Rathnapura (Kalu Ganga) | 6.61 | 🟡 Alert | 0.517 | 🔺 Rising |
| 2026-06-12 19:07:43 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.030 |  |
| 2026-06-12 19:07:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-12 19:06:48 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-12 19:06:22 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:06:12 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:05:58 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:05:56 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:05:34 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-12 19:05:22 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.019 |  |
| 2026-06-12 19:05:21 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.010 |  |
| 2026-06-12 19:05:20 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 19:05:19 | Baddegama (Gin Ganga) | 2.92 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-12 19:05:17 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.057 |  |
| 2026-06-12 19:05:13 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.420 | 🔺 Rising |
| 2026-06-12 19:04:51 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-12 19:04:33 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-06-12 19:04:09 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 19:03:46 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:03:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:02:41 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:02:36 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 19:02:33 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 19:02:31 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-12 19:02:21 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-12 19:02:16 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-06-12 19:01:56 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:01:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:01:31 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-06-12 19:01:30 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-12 19:01:29 | Nawalapitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.072 |  |
| 2026-06-12 19:01:27 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.104 |  |
| 2026-06-12 19:01:02 | Magura (Kalu Ganga) | 4.67 | 🟡 Alert | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 19:07:49 | Rathnapura (Kalu Ganga) | 6.61 | 🟡 Alert | 0.517 | 🔺 Rising |
| 2026-06-12 19:30:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.056 | 🔺 Rising |
| 2026-06-12 19:01:02 | Magura (Kalu Ganga) | 4.67 | 🟡 Alert | -0.010 |  |
| 2026-06-12 19:05:13 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.420 | 🔺 Rising |
| 2026-06-12 19:06:48 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-12 19:05:34 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-12 19:18:54 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-12 19:01:30 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-12 19:04:51 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-12 19:02:21 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-12 19:05:19 | Baddegama (Gin Ganga) | 2.92 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-12 19:02:36 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 19:02:33 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 19:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 19:05:20 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 19:02:41 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:01:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:01:56 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:11:27 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:03:46 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:06:22 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:06:12 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:03:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:04:09 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:02:31 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-12 19:05:21 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.010 |  |
| 2026-06-12 19:05:22 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.019 |  |
| 2026-06-12 19:01:31 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-06-12 19:07:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-12 19:07:43 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.030 |  |
| 2026-06-12 19:02:16 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-06-12 19:04:33 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-06-12 19:05:17 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.057 |  |
| 2026-06-12 19:01:29 | Nawalapitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.072 |  |
| 2026-06-12 19:01:27 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)