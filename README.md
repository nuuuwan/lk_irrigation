# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_14:11:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,455 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 14:11:18 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 14:10:53 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:10:22 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:10:20 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:07:24 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:06:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-02-18 14:06:01 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 23.802 | 🔺 Rising |
| 2026-02-18 14:05:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:05:32 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 14:05:19 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-18 14:04:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:58 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-18 14:04:47 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-02-18 14:04:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:33 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:04 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:00 | Thawalama (Gin Ganga) | 0.22 | 🟢 Normal | 23.802 | 🔺 Rising |
| 2026-02-18 14:03:53 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:03:17 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-18 14:03:13 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-02-18 14:03:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:03:09 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:03:09 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:02:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:34 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 14:02:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:29 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:19 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-02-18 14:02:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:09 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 14:01:53 | Padiyathalawa (Maduru Oya) | 1.63 | 🟢 Normal | -0.222 |  |
| 2026-02-18 14:01:51 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | -0.020 |  |
| 2026-02-18 14:01:32 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.061 |  |
| 2026-02-18 14:01:12 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:01:07 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:00:46 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:00:30 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:00:23 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:00:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.086 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 14:06:01 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 23.802 | 🔺 Rising |
| 2026-02-18 14:04:47 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-02-18 14:02:19 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-02-18 14:06:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-02-18 14:00:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-18 14:04:58 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-18 14:05:32 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 14:02:34 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 14:03:17 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-18 14:05:19 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-18 13:05:06 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 14:11:18 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 14:01:07 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:01:12 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:04 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:10:20 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:10:22 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:10:53 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:29 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:07:24 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:05:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:02:09 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:03:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:00:30 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:04:33 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-18 14:03:09 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:03:53 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:00:23 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:03:09 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-18 14:01:51 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | -0.020 |  |
| 2026-02-18 14:03:13 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-02-18 14:01:32 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.061 |  |
| 2026-02-18 14:01:53 | Padiyathalawa (Maduru Oya) | 1.63 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)