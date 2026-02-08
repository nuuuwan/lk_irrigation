# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_11:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 11:22:38 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-08 11:20:21 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-08 11:13:03 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-02-08 11:12:57 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:12:52 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.036 |  |
| 2026-02-08 11:11:29 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:11:03 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-08 11:10:08 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.127 |  |
| 2026-02-08 11:09:46 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:08:30 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:07:22 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-02-08 11:07:07 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-02-08 11:06:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:06:09 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:05:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:04:00 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-02-08 11:04:00 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.019 |  |
| 2026-02-08 11:03:37 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-08 11:03:29 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-08 11:03:16 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:03:09 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:03:02 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.061 |  |
| 2026-02-08 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:02:52 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:02:45 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:02:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:02:32 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:02:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-08 11:02:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:02:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:01:24 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-02-08 11:01:19 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 11:01:15 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:00:56 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:00:40 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:00:34 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:00:24 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 11:02:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-08 11:22:38 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-08 11:11:03 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-08 11:20:21 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-08 11:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 11:02:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:03:09 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:01:15 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:11:29 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:08:30 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:12:57 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:05:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:09:46 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:02:45 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:01:19 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:00:56 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:06:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:02:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:06:09 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:00:34 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:02:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:03:16 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 11:07:07 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-02-08 11:13:03 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-02-08 11:07:22 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-02-08 11:02:32 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:02:52 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:00:40 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:00:24 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-02-08 11:01:24 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-02-08 11:04:00 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-02-08 11:04:00 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.019 |  |
| 2026-02-08 11:03:29 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-08 11:03:37 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-08 11:12:52 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.036 |  |
| 2026-02-08 11:03:02 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.061 |  |
| 2026-02-08 11:10:08 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.127 |  |
| 2026-02-08 09:10:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)