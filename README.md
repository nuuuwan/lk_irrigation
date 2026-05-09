# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_02:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 02:15:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-10 02:08:43 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-05-10 02:07:15 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-10 02:06:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:06:31 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-10 02:05:02 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.190 |  |
| 2026-05-10 02:04:29 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:04:25 | Katharagama (Menik Ganga) | 1.54 | 🟢 Normal | -0.033 |  |
| 2026-05-10 02:04:11 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.048 |  |
| 2026-05-10 02:04:06 | Moragaswewa (Deduru Oya) | 3.62 | 🟢 Normal | -0.079 |  |
| 2026-05-10 02:03:59 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-10 02:03:24 | Wellawaya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.051 |  |
| 2026-05-10 02:02:51 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:02:40 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-05-10 02:02:36 | Nakkala (Kumbukkan Oya) | 2.40 | 🟢 Normal | -0.150 |  |
| 2026-05-10 02:02:31 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 02:02:29 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-10 02:01:55 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:43 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-05-10 02:01:43 | Kuda Oya (Kirindi Oya) | 2.29 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-10 02:01:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:21 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 02:01:19 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-05-10 02:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.036 |  |
| 2026-05-10 02:00:54 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-10 02:00:45 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.055 |  |
| 2026-05-10 01:50:26 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-05-10 01:30:09 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 02:03:59 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-10 02:01:43 | Kuda Oya (Kirindi Oya) | 2.29 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-10 02:00:54 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-10 02:01:21 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 02:15:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-10 02:06:31 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-10 02:04:29 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:55 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:02:51 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:08:13 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:06:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:30:09 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:03:44 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:21:13 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.008 |  |
| 2026-05-10 02:08:43 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-05-10 02:02:31 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 02:02:29 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-10 02:01:19 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-05-10 01:21:31 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.032 |  |
| 2026-05-10 02:04:25 | Katharagama (Menik Ganga) | 1.54 | 🟢 Normal | -0.033 |  |
| 2026-05-10 02:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.036 |  |
| 2026-05-10 02:07:15 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-10 01:04:22 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-05-10 02:04:11 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.048 |  |
| 2026-05-10 02:02:40 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-05-10 00:17:52 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 02:03:24 | Wellawaya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.051 |  |
| 2026-05-10 02:00:45 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.055 |  |
| 2026-05-10 02:01:43 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-05-10 01:02:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-05-10 02:04:06 | Moragaswewa (Deduru Oya) | 3.62 | 🟢 Normal | -0.079 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-10 01:01:13 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.103 |  |
| 2026-05-10 02:02:36 | Nakkala (Kumbukkan Oya) | 2.40 | 🟢 Normal | -0.150 |  |
| 2026-05-10 02:05:02 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.190 |  |
| 2026-05-10 00:45:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -4.800 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)