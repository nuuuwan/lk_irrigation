# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_08:31:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,897 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 08:31:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2025-12-20 08:14:11 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2025-12-20 08:12:52 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:12:20 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:10:39 | Horowpothana (Yan Oya) | 6.34 | 🟡 Alert | -0.009 |  |
| 2025-12-20 08:10:37 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:10:35 | Galgamuwa (Mee Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:10:33 | Galgamuwa (Mee Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:08:50 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 08:07:29 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:07:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:06:52 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:06:17 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:05:45 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:05:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2025-12-20 08:05:04 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 08:04:52 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:04:45 | Manampitiya (Mahaweli Ganga) | 4.13 | 🟡 Alert | -0.030 |  |
| 2025-12-20 08:04:34 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:04:30 | Thanthirimale (Malwathu Oya) | 5.60 | 🟡 Alert | 0.000 |  |
| 2025-12-20 08:04:28 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:04:18 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:04:08 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 08:03:50 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2025-12-20 08:03:42 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-20 08:03:35 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:03:13 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:03:07 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:02:34 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:02:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:02:22 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:02:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.100 |  |
| 2025-12-20 08:01:29 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-20 08:01:20 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 08:01:19 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:01:12 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:01:10 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2025-12-20 08:00:56 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-20 08:00:52 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:00:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 08:04:30 | Thanthirimale (Malwathu Oya) | 5.60 | 🟡 Alert | 0.000 |  |
| 2025-12-20 08:10:39 | Horowpothana (Yan Oya) | 6.34 | 🟡 Alert | -0.009 |  |
| 2025-12-20 08:04:45 | Manampitiya (Mahaweli Ganga) | 4.13 | 🟡 Alert | -0.030 |  |
| 2025-12-20 08:08:50 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 08:04:08 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 08:00:56 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-20 08:01:20 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 08:05:04 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 08:10:37 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:01:12 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:12:52 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:12:20 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:10:35 | Galgamuwa (Mee Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:06:17 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:05:45 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:02:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:01:19 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:03:35 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:00:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:04:28 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:04:18 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:07:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:14:11 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2025-12-20 08:07:29 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:02:22 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:02:34 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:03:13 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:04:34 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:04:52 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:02:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:00:52 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:01:29 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-20 08:03:50 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2025-12-20 08:03:42 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-20 08:31:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2025-12-20 08:01:10 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2025-12-20 08:05:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2025-12-20 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.100 |  |
| 2025-12-20 07:07:31 | Weraganthota (Mahaweli Ganga) | -0.52 | 🟢 Normal | -0.373 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)