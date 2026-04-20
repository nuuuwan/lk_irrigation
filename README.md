# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_21:19:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 21:19:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-04-20 21:11:54 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:10:48 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-20 21:10:13 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-04-20 21:09:51 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-20 21:09:15 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-20 21:09:15 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-20 21:07:59 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:07:45 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-20 21:07:43 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 21:07:42 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 21:07:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-20 21:06:49 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-20 21:05:59 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-04-20 21:05:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.118 |  |
| 2026-04-20 21:05:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.069 |  |
| 2026-04-20 21:05:12 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-04-20 21:05:03 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-20 21:04:40 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.164 |  |
| 2026-04-20 21:03:48 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 21:03:37 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 21:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:03:20 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 21:03:06 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 21:03:01 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.044 |  |
| 2026-04-20 21:02:53 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.044 |  |
| 2026-04-20 21:02:46 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-20 21:02:28 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:02:20 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:02:19 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-04-20 21:02:12 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 21:02:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:01:42 | Kuda Oya (Kirindi Oya) | 4.25 | 🟢 Normal | 2.990 | 🔺 Rising |
| 2026-04-20 21:01:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:00:43 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.307 |  |
| 2026-04-20 20:55:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 21:01:42 | Kuda Oya (Kirindi Oya) | 4.25 | 🟢 Normal | 2.990 | 🔺 Rising |
| 2026-04-20 21:10:13 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-04-20 21:05:59 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-04-20 21:05:12 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 21:09:15 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-20 21:06:49 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-20 21:05:03 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-20 21:07:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-20 21:07:45 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-20 21:02:46 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-20 21:09:15 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-20 21:09:51 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-20 21:03:48 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 21:03:20 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 21:07:42 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 21:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 21:10:48 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-20 21:07:43 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 21:03:06 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 21:02:12 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 21:03:37 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:01:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:07:59 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:11:54 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:02:20 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:02:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:02:28 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-20 21:02:19 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-04-20 21:02:53 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.044 |  |
| 2026-04-20 21:03:01 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.044 |  |
| 2026-04-20 21:19:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-04-20 21:05:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.069 |  |
| 2026-04-20 21:05:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.118 |  |
| 2026-04-20 21:04:40 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.164 |  |
| 2026-04-20 21:00:43 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.307 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)