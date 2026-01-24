# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_10:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,247 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 10:15:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.042 |  |
| 2026-01-24 10:15:01 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:12:44 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-01-24 10:08:08 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:07:32 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-01-24 10:06:57 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.037 |  |
| 2026-01-24 10:06:32 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.105 |  |
| 2026-01-24 10:05:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:05:04 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:05:00 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:04:59 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 10:04:05 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:58 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:37 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-24 10:03:32 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:26 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:11 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 10:03:01 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:45 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:41 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.083 |  |
| 2026-01-24 10:02:38 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-01-24 10:02:21 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 10:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-01-24 10:02:12 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-24 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.051 |  |
| 2026-01-24 10:02:03 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:02 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:02 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:59 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-24 10:01:14 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:09 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-01-24 10:00:58 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:00:47 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:00:40 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.010 |  |
| 2026-01-24 10:00:21 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 10:03:37 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-24 10:03:11 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 10:02:21 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 10:04:59 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 10:00:21 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:45 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:00:47 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:08:08 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:05:04 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:01 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:58 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:04:05 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:14 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:08:49 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:15:01 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:32 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:02 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:03 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:05:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:05:00 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:03:26 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:02:02 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:01:09 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 10:12:44 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-01-24 10:07:32 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-01-24 10:02:12 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-24 10:00:40 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.010 |  |
| 2026-01-24 10:02:38 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-01-24 10:01:59 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-24 10:06:57 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.037 |  |
| 2026-01-24 10:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-01-24 10:15:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.042 |  |
| 2026-01-24 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.051 |  |
| 2026-01-24 10:01:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-01-24 10:02:41 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.083 |  |
| 2026-01-24 10:06:32 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)