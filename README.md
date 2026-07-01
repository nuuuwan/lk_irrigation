# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_20:16:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 20:16:06 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.017 |  |
| 2026-07-01 20:11:47 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-07-01 20:09:32 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:07:54 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:07:49 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-07-01 20:07:33 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:06:03 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:06:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.069 |  |
| 2026-07-01 20:06:02 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-07-01 20:05:38 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.059 |  |
| 2026-07-01 20:05:36 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.019 |  |
| 2026-07-01 20:05:26 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:05:25 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:04:31 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:04:10 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-07-01 20:04:03 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:04:00 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:03:37 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-01 20:03:19 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:03:11 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:03:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-07-01 20:02:47 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-01 20:02:45 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:02:33 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:02:25 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.061 |  |
| 2026-07-01 20:02:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.016 |  |
| 2026-07-01 20:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.022 |  |
| 2026-07-01 20:02:04 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:48 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:46 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:32 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:17 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.027 |  |
| 2026-07-01 20:00:50 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.061 |  |
| 2026-07-01 20:00:14 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 20:03:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-07-01 20:07:49 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-07-01 20:02:47 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:04:03 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:03:11 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:48 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:03:37 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:06:03 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:04:31 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:00:14 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:32 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:03:19 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:05:25 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:07:54 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:02:04 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:05:26 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:09:32 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:01:46 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 20:06:02 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-07-01 20:02:45 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:07:33 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:02:33 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:04:00 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.010 |  |
| 2026-07-01 20:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-01 20:11:47 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-07-01 20:02:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.016 |  |
| 2026-07-01 20:16:06 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.017 |  |
| 2026-07-01 20:05:36 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.019 |  |
| 2026-07-01 20:04:10 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-07-01 20:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.022 |  |
| 2026-07-01 20:01:17 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.027 |  |
| 2026-07-01 20:05:38 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.059 |  |
| 2026-07-01 20:00:50 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.061 |  |
| 2026-07-01 20:02:25 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.061 |  |
| 2026-07-01 20:06:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)