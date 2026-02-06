# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_23:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,044 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 23:14:30 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:12:16 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:11:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:10:17 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-02-06 23:09:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-02-06 23:09:28 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-06 23:08:49 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-06 23:08:26 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:07:24 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-06 23:06:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-02-06 23:05:45 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:43 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:36 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:06 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:03 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-06 23:04:02 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-02-06 23:04:01 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-02-06 23:03:40 | Horowpothana (Yan Oya) | 3.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 23:03:26 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.100 |  |
| 2026-02-06 23:03:19 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:03:12 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:03:01 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.022 |  |
| 2026-02-06 23:02:46 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:40 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-06 23:02:31 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:25 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:04 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:00 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-06 23:01:46 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:01:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-06 23:01:33 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 23:01:26 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:00:41 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 22:48:52 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.075 |  |
| 2026-02-06 22:40:23 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 23:04:02 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-02-06 23:09:28 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 23:08:49 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-06 23:06:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-02-06 23:02:40 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-06 23:01:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-06 23:07:24 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-06 23:01:33 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 23:03:40 | Horowpothana (Yan Oya) | 3.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 23:01:26 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 22:01:28 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:05:45 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:06 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:36 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:03:12 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:03:19 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:14:30 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:11:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:25 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 22:11:13 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:31 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:04 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:04:43 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:12:16 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:01:46 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:02:46 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 23:10:17 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-02-06 23:04:03 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-06 23:02:00 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-06 23:03:01 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.022 |  |
| 2026-02-06 23:09:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-06 22:48:52 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.075 |  |
| 2026-02-06 23:03:26 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)