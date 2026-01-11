# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_20:12:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,981 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 20:12:10 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:11:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:10:08 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-01-11 20:07:51 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-01-11 20:07:47 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:06:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-01-11 20:06:09 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 20:05:59 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:05:06 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:05:02 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 20:04:59 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-11 20:04:48 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:04:37 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:04:32 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-11 20:04:14 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:04:07 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.040 |  |
| 2026-01-11 20:04:05 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 20:03:51 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.036 |  |
| 2026-01-11 20:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-01-11 20:03:41 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:03:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:32 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:03:30 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:18 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.059 |  |
| 2026-01-11 20:03:10 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:03:02 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:02 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-11 20:02:50 | Siyambalanduwa (Heda Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-11 20:02:40 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:02:10 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-01-11 20:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:01:58 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 20:01:57 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:01:55 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:00:53 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:00:23 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:23:09 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:22:50 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 20:03:02 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-11 20:04:59 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-11 20:04:32 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-11 20:02:50 | Siyambalanduwa (Heda Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 20:01:58 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 20:04:05 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 20:06:09 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 20:05:02 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 20:03:10 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:03:32 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:03:41 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:07:47 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 20:02:40 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:00:53 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:01:57 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:05:59 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:12:10 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:30 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:05:06 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:04:48 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:04:37 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:00:23 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:51 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:03:02 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:11:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:01:55 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:10:08 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-01-11 20:02:10 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-01-11 20:06:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-01-11 20:07:51 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-01-11 20:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-01-11 20:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.036 |  |
| 2026-01-11 20:04:07 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.040 |  |
| 2026-01-11 20:03:18 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)