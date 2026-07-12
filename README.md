# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_13:17:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,249 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 13:17:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-07-12 13:16:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:14:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:08:47 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:08:19 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:07:43 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:07:38 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-07-12 13:07:11 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-07-12 13:07:04 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-07-12 13:07:01 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:06:53 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:06:09 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:05:33 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.049 |  |
| 2026-07-12 13:05:26 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.019 |  |
| 2026-07-12 13:05:18 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.032 |  |
| 2026-07-12 13:05:16 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.107 |  |
| 2026-07-12 13:05:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-12 13:05:00 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-12 13:04:46 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-07-12 13:04:12 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:04:09 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-12 13:03:59 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:03:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-12 13:03:44 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-07-12 13:03:18 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:03:10 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-07-12 13:03:04 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:02:20 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:02:10 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.010 |  |
| 2026-07-12 13:01:58 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:58 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:57 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:54 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-07-12 13:01:47 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:45 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:27 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-07-12 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:07 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-07-12 13:00:52 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 13:04:09 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-12 13:05:00 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-12 13:05:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-12 13:03:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-12 13:03:18 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:04:12 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:47 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:00:52 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:06:09 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:07:43 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:58 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:03:59 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:03:04 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:58 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:16:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:08:19 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:02:20 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:06:53 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:08:47 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:07:01 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:57 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:14:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:45 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:07:11 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-07-12 13:07:38 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-07-12 13:02:10 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.010 |  |
| 2026-07-12 13:01:54 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-07-12 13:03:10 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-07-12 13:01:07 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-07-12 13:07:04 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-07-12 13:05:26 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.019 |  |
| 2026-07-12 13:01:27 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-07-12 13:03:44 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-07-12 13:04:46 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-07-12 13:05:18 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.032 |  |
| 2026-07-12 13:05:33 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.049 |  |
| 2026-07-12 13:17:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-07-12 13:05:16 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)