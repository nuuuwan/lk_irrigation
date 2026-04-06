# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_08:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 08:17:20 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:14:22 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 08:10:51 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-04-06 08:10:10 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:08:11 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-04-06 08:07:14 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:06:57 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 08:06:56 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-04-06 08:06:35 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.048 |  |
| 2026-04-06 08:06:32 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:06:22 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:42 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-06 08:05:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-04-06 08:05:35 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:28 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:23 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-06 08:05:15 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.101 |  |
| 2026-04-06 08:05:02 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:04:59 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 08:04:52 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.071 |  |
| 2026-04-06 08:04:22 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:03:57 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-06 08:03:26 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-06 08:03:16 | Deraniyagala (Kelani Ganga) | 12.00 | 🔴 Major Flood | 11.607 | 🔺 Rising |
| 2026-04-06 08:03:02 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.160 |  |
| 2026-04-06 08:03:01 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 08:02:53 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-04-06 08:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:02:26 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.060 |  |
| 2026-04-06 08:01:57 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:01:45 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-06 08:01:09 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-06 08:01:01 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-04-06 08:00:35 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | -0.118 |  |
| 2026-04-06 08:00:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 08:03:16 | Deraniyagala (Kelani Ganga) | 12.00 | 🔴 Major Flood | 11.607 | 🔺 Rising |
| 2026-04-06 08:05:42 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-06 08:03:26 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-06 08:06:57 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 08:04:59 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 08:05:23 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-06 08:03:01 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 08:14:22 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 08:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:01:57 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:00:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:35 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-06 07:02:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:28 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:01:45 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:02:26 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:04:22 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:06:22 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:06:32 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:07:14 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:05:02 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:17:20 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:10:10 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 08:03:57 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-06 08:01:01 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-04-06 08:01:09 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-06 08:08:11 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-04-06 08:05:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-04-06 08:02:53 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-04-06 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-06 08:10:51 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-04-06 08:06:56 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-04-06 08:06:35 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.048 |  |
| 2026-04-06 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.060 |  |
| 2026-04-06 08:04:52 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.071 |  |
| 2026-04-06 08:05:15 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.101 |  |
| 2026-04-06 08:00:35 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | -0.118 |  |
| 2026-04-06 08:03:02 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)