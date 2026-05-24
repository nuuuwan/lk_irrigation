# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_17:46:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 17:46:26 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:23:39 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:13:19 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:13:18 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:09:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-05-24 17:09:28 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-05-24 17:08:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:08:24 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-05-24 17:08:18 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 17:08:09 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 17:06:24 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:06:18 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 17:06:14 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-05-24 17:05:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:05:44 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-05-24 17:05:23 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:05:21 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:04:58 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:04:44 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.040 |  |
| 2026-05-24 17:04:44 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-24 17:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.26 | 🟡 Alert | -0.040 |  |
| 2026-05-24 17:04:21 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:04:20 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:04:00 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:03:49 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.098 |  |
| 2026-05-24 17:03:17 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-05-24 17:03:11 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:03:10 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:03:02 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 17:02:55 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:02:49 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-24 17:02:33 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:02:26 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:01:55 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-24 17:01:33 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:01:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:01:15 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:00:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-05-24 17:00:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 17:06:18 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 17:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.26 | 🟡 Alert | -0.040 |  |
| 2026-05-24 17:05:44 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-05-24 17:09:28 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-05-24 17:01:55 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-24 17:02:49 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-24 17:03:02 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 17:08:09 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 17:08:18 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 17:03:10 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:04:30 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:00:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:01:33 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:04:00 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:01:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:06:24 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:03:11 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:05:23 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:46:26 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:08:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:02:55 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:13:19 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:05:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:04:58 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:04:21 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:08:24 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-05-24 17:01:15 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:02:26 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:05:21 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:02:33 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | -0.010 |  |
| 2026-05-24 17:03:17 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-05-24 17:00:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-05-24 17:06:14 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-05-24 17:09:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-05-24 17:04:44 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-24 17:04:44 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.040 |  |
| 2026-05-24 17:03:49 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)