# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_05:11:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 05:11:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-08 05:08:31 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:08:06 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.013 |  |
| 2026-02-08 05:07:30 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:06:29 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:06:22 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-02-08 05:06:05 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:05:02 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 05:04:52 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:04:48 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -4.966 |  |
| 2026-02-08 05:04:45 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-08 05:04:44 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-08 05:04:32 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:04:31 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:04:28 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -108.000 |  |
| 2026-02-08 05:04:27 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -108.000 |  |
| 2026-02-08 05:04:19 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -4.966 |  |
| 2026-02-08 05:03:39 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:03:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:03:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-08 05:02:57 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-02-08 05:02:50 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-02-08 05:02:40 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.087 |  |
| 2026-02-08 05:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:02:04 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:02:04 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:01:49 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:01:22 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-08 05:01:21 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.282 |  |
| 2026-02-08 05:01:17 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.061 |  |
| 2026-02-08 05:01:16 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:00:58 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:00:38 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:00:09 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:58:44 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:42:23 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-08 04:22:49 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.179 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 05:06:22 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-02-08 04:42:23 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-08 05:04:44 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-08 03:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-08 05:11:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-08 05:04:45 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-08 05:05:02 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 05:00:09 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:02:04 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:01:49 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:04:32 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:04:56 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:06:29 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:04:31 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:00:58 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:02:04 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:03:39 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:07:23 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:07:30 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:08:31 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:03:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:01:16 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:04:52 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-08 05:01:22 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-08 05:03:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-08 05:02:50 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-02-08 05:08:06 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.013 |  |
| 2026-02-08 02:11:27 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-08 05:02:57 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-02-08 03:05:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-02-08 05:01:17 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.061 |  |
| 2026-02-08 05:02:40 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.087 |  |
| 2026-02-08 05:01:21 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.282 |  |
| 2026-02-08 05:04:48 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -4.966 |  |
| 2026-02-08 05:04:28 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)