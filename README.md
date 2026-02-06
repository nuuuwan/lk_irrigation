# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_18:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 18:12:32 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:09:34 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-06 18:06:47 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:45 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:39 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:01 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:59 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:54 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 3708.000 | 🔺 Rising |
| 2026-02-06 18:04:53 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 3708.000 | 🔺 Rising |
| 2026-02-06 18:04:51 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 3708.000 | 🔺 Rising |
| 2026-02-06 18:04:42 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:36 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:27 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.059 |  |
| 2026-02-06 18:04:01 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-06 18:03:58 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-06 18:03:57 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:02 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 18:02:59 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:45 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:41 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 18:02:40 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:29 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:21 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-06 18:02:14 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-06 18:02:13 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-06 18:02:08 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 18:02:07 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-06 18:01:37 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:01:14 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-06 18:01:04 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 18:01:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2026-02-06 18:00:20 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 17:59:07 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:26:12 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:25:40 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 18:04:54 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 3708.000 | 🔺 Rising |
| 2026-02-06 18:04:01 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-06 18:03:58 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 18:01:04 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 18:01:14 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-06 17:25:40 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-06 18:02:14 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-06 18:09:34 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-06 18:03:02 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 18:02:08 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 18:00:20 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 18:02:41 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 18:02:29 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:40 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:01 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:59 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:07 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:01:37 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:59 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:47 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:36 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:57 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:39 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:42 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:45 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 17:26:12 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:45 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:12:32 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:21 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-06 17:02:21 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-06 18:02:13 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-06 18:04:27 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.059 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 18:01:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)