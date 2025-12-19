# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_03:29:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 03:29:10 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:12:03 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:11:51 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-20 03:11:32 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:10:29 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:10:28 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:09:25 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.035 |  |
| 2025-12-20 03:09:18 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:08:37 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-20 03:08:14 | Glencourse (Kelani Ganga) | 9.01 | 🟢 Normal | -0.082 |  |
| 2025-12-20 03:07:24 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.049 |  |
| 2025-12-20 03:05:37 | Manampitiya (Mahaweli Ganga) | 4.23 | 🟡 Alert | -0.020 |  |
| 2025-12-20 03:05:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:05:29 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:05:22 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 03:05:19 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:04:50 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.011 |  |
| 2025-12-20 03:03:48 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2025-12-20 03:03:46 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:03:23 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:03:03 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-20 03:02:30 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2025-12-20 03:02:30 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.061 |  |
| 2025-12-20 03:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:49 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-20 03:01:48 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.036 |  |
| 2025-12-20 03:01:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-20 03:01:23 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:01:14 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:59:54 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-20 02:04:29 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 03:05:37 | Manampitiya (Mahaweli Ganga) | 4.23 | 🟡 Alert | -0.020 |  |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-20 03:08:37 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-20 03:11:51 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-20 03:01:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-20 01:09:42 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 03:03:03 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-20 03:05:22 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 01:00:28 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:14 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:05:19 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:08:58 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:03:23 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:10:29 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:05:29 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:12:03 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:29:10 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:48 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:11:32 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:59:54 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:09:18 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:03:46 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:05:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:10:28 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:01:23 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:02:30 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-20 03:03:48 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2025-12-20 03:04:50 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.011 |  |
| 2025-12-20 03:01:49 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-20 03:02:30 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2025-12-20 03:09:25 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.035 |  |
| 2025-12-20 03:01:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.036 |  |
| 2025-12-20 03:07:24 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.049 |  |
| 2025-12-20 03:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.061 |  |
| 2025-12-20 03:08:14 | Glencourse (Kelani Ganga) | 9.01 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)