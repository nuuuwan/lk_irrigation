# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_05:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 05:14:16 | Rathnapura (Kalu Ganga) | 6.50 | 🟡 Alert | 1.563 | 🔺 Rising |
| 2026-05-22 05:11:43 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-05-22 05:11:21 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-22 05:11:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:10:48 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | 1.130 | 🔺 Rising |
| 2026-05-22 05:09:29 | Glencourse (Kelani Ganga) | 13.36 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-05-22 05:08:23 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-22 05:07:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:07:08 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-22 05:06:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-22 05:06:33 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:06:19 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-22 05:05:53 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-05-22 05:05:38 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.065 |  |
| 2026-05-22 05:05:19 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.051 |  |
| 2026-05-22 05:05:16 | Deraniyagala (Kelani Ganga) | 4.16 | 🟢 Normal | 0.618 | 🔺 Rising |
| 2026-05-22 05:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-05-22 05:04:34 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-22 05:04:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:04:23 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-05-22 05:03:54 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 05:03:52 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:03:47 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-22 05:03:05 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-05-22 05:02:07 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:48 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:23 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:19 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:14 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:00 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:00:43 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-22 05:00:30 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:41:39 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.051 |  |
| 2026-05-22 04:31:46 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 05:14:16 | Rathnapura (Kalu Ganga) | 6.50 | 🟡 Alert | 1.563 | 🔺 Rising |
| 2026-05-22 05:10:48 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | 1.130 | 🔺 Rising |
| 2026-05-22 05:09:29 | Glencourse (Kelani Ganga) | 13.36 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-05-22 05:05:16 | Deraniyagala (Kelani Ganga) | 4.16 | 🟢 Normal | 0.618 | 🔺 Rising |
| 2026-05-22 05:03:05 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-05-22 05:05:53 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-05-22 05:04:23 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-05-22 05:11:43 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-05-22 05:08:23 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-22 05:03:47 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-22 05:06:19 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-22 05:04:34 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-22 05:06:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-22 04:15:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-22 05:07:08 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-22 04:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-22 05:11:21 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-22 05:03:54 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 05:00:43 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-22 05:01:48 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:00 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:02:07 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:07:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:04:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:06:33 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:19 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:00:30 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:03:52 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:11:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:23 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 05:01:14 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:02:24 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:13:13 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-05-22 05:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-22 05:05:19 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.051 |  |
| 2026-05-22 05:05:38 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)