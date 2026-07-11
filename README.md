# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_15:08:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 15:08:54 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-07-11 15:08:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:07:50 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:07:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-11 15:06:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-11 15:06:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:05:45 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.009 |  |
| 2026-07-11 15:05:33 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-11 15:05:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:05:06 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:04:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.061 |  |
| 2026-07-11 15:04:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-11 15:04:01 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:04:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:03:57 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:03:50 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:03:49 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:03:41 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-07-11 15:03:35 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.012 |  |
| 2026-07-11 15:03:18 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-11 15:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-07-11 15:02:57 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:02:56 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:02:52 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-11 15:02:48 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:02:43 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.060 |  |
| 2026-07-11 15:02:15 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-11 15:02:08 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-11 15:02:08 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-07-11 15:01:53 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:01:36 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:26 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:19 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:16 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:12 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:11 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:00:20 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 15:02:15 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-11 15:02:52 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-11 15:02:08 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-11 15:05:33 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-11 15:06:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-11 15:03:18 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-11 15:07:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-11 15:01:11 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:05:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:26 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:02:57 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:00:20 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:03:49 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:12 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:02:48 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:07:50 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:01:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:08:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:04:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:36 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:04:01 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:16 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:02:43 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:06:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:18:36 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:05:06 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:05:45 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.009 |  |
| 2026-07-11 15:03:57 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:01:53 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:03:50 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:02:56 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:02:08 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-07-11 15:03:35 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.012 |  |
| 2026-07-11 15:08:54 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-07-11 15:04:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-11 15:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-07-11 15:03:41 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-07-11 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.060 |  |
| 2026-07-11 15:04:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)