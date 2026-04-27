# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_08:26:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,259 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 08:26:35 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:21:00 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-04-27 08:17:14 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:16:40 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:16:38 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:15:40 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-04-27 08:14:29 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-04-27 08:13:01 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-27 08:12:55 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:12:54 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:11:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:09:47 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:06:07 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:05:48 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:05:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 08:04:16 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.085 |  |
| 2026-04-27 08:04:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:04:03 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-27 08:03:57 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-27 08:03:39 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-27 08:03:21 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 08:02:51 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:44 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.022 |  |
| 2026-04-27 08:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:33 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-27 08:02:22 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:21 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:17 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-27 08:02:17 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.024 |  |
| 2026-04-27 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-04-27 08:02:04 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 08:01:59 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:53 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-27 08:01:21 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.124 |  |
| 2026-04-27 08:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:08 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-04-27 08:00:31 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.091 |  |
| 2026-04-27 08:00:19 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-27 08:00:15 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-04-27 08:00:11 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 08:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-27 08:03:39 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-27 08:13:01 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-27 08:03:57 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-27 08:02:17 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-27 08:00:19 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-27 08:05:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 08:03:21 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 08:02:04 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 08:12:55 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:06:07 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:59 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:04:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:26:35 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:01:53 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:11:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:22 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:51 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:17:14 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:16:40 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:09:47 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:02:21 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-27 08:14:29 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-04-27 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-04-27 08:04:03 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-27 08:21:00 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-04-27 07:01:17 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.015 |  |
| 2026-04-27 08:00:15 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-04-27 08:02:33 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-27 08:01:08 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-04-27 08:02:44 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.022 |  |
| 2026-04-27 08:02:17 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.024 |  |
| 2026-04-27 08:15:40 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-04-27 08:00:11 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.043 |  |
| 2026-04-27 08:04:16 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.085 |  |
| 2026-04-27 08:00:31 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.091 |  |
| 2026-04-27 08:01:21 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)