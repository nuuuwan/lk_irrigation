# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_21:19:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 21:19:31 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:17:56 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-25 21:16:03 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-05-25 21:15:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:11:51 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:09:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:08:25 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-05-25 21:08:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:08:04 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:07:48 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:07:21 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 21:07:05 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.224 |  |
| 2026-05-25 21:05:19 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:04:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:04:56 | Ellagawa (Kalu Ganga) | 8.75 | 🟢 Normal | -0.028 |  |
| 2026-05-25 21:04:53 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-25 21:04:33 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 21:04:08 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-25 21:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:03:33 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:03:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:03:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:03:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:02:52 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-25 21:02:51 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 21:02:38 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.051 |  |
| 2026-05-25 21:02:17 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:02:17 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:02:14 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:02:06 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:01:56 | Hanwella (Kelani Ganga) | 4.09 | 🟢 Normal | -0.066 |  |
| 2026-05-25 21:01:54 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 21:01:31 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 21:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:01:15 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.024 |  |
| 2026-05-25 21:00:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:00:26 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 20:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.061 |  |
| 2026-05-25 21:04:08 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-25 21:04:53 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-25 21:17:56 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-25 21:02:52 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-25 21:01:54 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 21:01:31 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 21:02:51 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 21:07:21 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 21:04:33 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 21:02:06 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:04:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:07:48 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:19:31 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:03:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:09:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:11:51 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:00:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:05:19 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:08:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:15:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:00:26 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:03:33 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:02:14 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:16:03 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-05-25 21:08:25 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-05-25 21:08:04 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:03:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:02:17 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-25 21:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 21:01:15 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.024 |  |
| 2026-05-25 21:04:56 | Ellagawa (Kalu Ganga) | 8.75 | 🟢 Normal | -0.028 |  |
| 2026-05-25 21:02:38 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.051 |  |
| 2026-05-25 21:01:56 | Hanwella (Kelani Ganga) | 4.09 | 🟢 Normal | -0.066 |  |
| 2026-05-25 21:07:05 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)