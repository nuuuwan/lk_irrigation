# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_04:04:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 04:04:19 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-05-25 04:03:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:03:44 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.049 |  |
| 2026-05-25 04:03:18 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-25 04:03:12 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-05-25 04:03:03 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.025 |  |
| 2026-05-25 04:02:57 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-25 04:02:41 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-05-25 04:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.024 |  |
| 2026-05-25 04:02:06 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.052 |  |
| 2026-05-25 04:01:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.085 |  |
| 2026-05-25 04:01:35 | Ellagawa (Kalu Ganga) | 9.23 | 🟢 Normal | -0.052 |  |
| 2026-05-25 04:01:24 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.156 |  |
| 2026-05-25 04:01:00 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:00:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:18:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:18:02 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:14:06 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.025 |  |
| 2026-05-25 03:13:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | -0.024 |  |
| 2026-05-25 03:12:19 | Rathnapura (Kalu Ganga) | 5.17 | 🟢 Normal | -0.042 |  |
| 2026-05-25 03:12:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.024 |  |
| 2026-05-25 03:12:16 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:11:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | -0.024 |  |
| 2026-05-25 03:11:12 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-05-25 03:11:01 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | 0.239 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 03:08:17 | Putupaula (Kalu Ganga) | 3.22 | 🟡 Alert | -0.010 |  |
| 2026-05-25 04:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.024 |  |
| 2026-05-25 03:11:01 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-25 04:03:18 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-25 03:03:10 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:05:46 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:01:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:12:16 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:01:39 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:03:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:00:13 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:00:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:01:00 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:18:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 04:04:19 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:42 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:05:30 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-05-25 03:11:12 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-05-25 04:02:57 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-25 03:07:24 | Kithulgala (Kelani Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-05-25 04:03:12 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-05-25 04:03:03 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.025 |  |
| 2026-05-25 03:12:19 | Rathnapura (Kalu Ganga) | 5.17 | 🟢 Normal | -0.042 |  |
| 2026-05-25 04:03:44 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.049 |  |
| 2026-05-25 04:01:35 | Ellagawa (Kalu Ganga) | 9.23 | 🟢 Normal | -0.052 |  |
| 2026-05-25 04:02:06 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.052 |  |
| 2026-05-25 04:02:41 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-05-25 04:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-05-25 04:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.085 |  |
| 2026-05-25 03:09:33 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.097 |  |
| 2026-05-25 03:09:26 | Deraniyagala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.101 |  |
| 2026-05-25 04:01:24 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)