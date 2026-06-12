# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_00:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,795 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 00:16:52 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | -0.009 |  |
| 2026-06-13 00:16:32 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.107 |  |
| 2026-06-13 00:10:43 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.035 |  |
| 2026-06-13 00:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-06-13 00:07:52 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 00:07:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:07:01 | Glencourse (Kelani Ganga) | 12.32 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-13 00:06:11 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-06-13 00:06:11 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-13 00:05:30 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-13 00:05:23 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.078 |  |
| 2026-06-13 00:04:52 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 00:04:41 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-13 00:04:11 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 00:04:00 | Urawa (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.119 |  |
| 2026-06-13 00:03:50 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.049 |  |
| 2026-06-13 00:03:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 00:03:19 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 00:02:58 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | 10.588 | 🔺 Rising |
| 2026-06-13 00:02:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:49 | Giriulla (Maha Oya) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-06-13 00:02:44 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:41 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | 10.588 | 🔺 Rising |
| 2026-06-13 00:02:35 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 00:02:34 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-06-13 00:02:20 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-06-13 00:02:18 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:15 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-13 00:02:10 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-13 00:02:02 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:00:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 00:00:18 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:00:16 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 00:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-06-13 00:02:20 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-06-13 00:05:23 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.078 |  |
| 2026-06-13 00:02:58 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | 10.588 | 🔺 Rising |
| 2026-06-13 00:02:15 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-13 00:05:30 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-13 00:02:10 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-13 00:07:01 | Glencourse (Kelani Ganga) | 12.32 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-13 00:06:11 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-12 22:06:30 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-13 00:03:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 00:00:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 00:04:52 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-13 00:02:35 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 00:03:19 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 00:00:16 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 00:07:52 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 00:04:11 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:00:18 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:18 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:07:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:44 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:02 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:16:52 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | -0.009 |  |
| 2026-06-13 00:04:41 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-13 00:06:11 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-06-13 00:02:34 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-06-13 00:02:49 | Giriulla (Maha Oya) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-06-13 00:10:43 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.035 |  |
| 2026-06-13 00:03:50 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.049 |  |
| 2026-06-13 00:16:32 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.107 |  |
| 2026-06-13 00:04:00 | Urawa (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)