# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_09:25:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,478 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 09:25:24 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:13:19 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:10:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:10:07 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-06 09:09:51 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:08:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-06 09:07:35 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:07:33 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:06:18 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:06:18 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:06:12 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-02-06 09:05:51 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 09:05:35 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:05:29 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:04:41 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.039 |  |
| 2026-02-06 09:04:19 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.112 |  |
| 2026-02-06 09:03:57 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:03:55 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 09:03:19 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.166 |  |
| 2026-02-06 09:03:02 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 09:03:01 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:02:46 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-06 09:02:21 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 09:02:20 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-06 09:02:17 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:02:04 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:01:43 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:01:41 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-02-06 09:01:04 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.198 |  |
| 2026-02-06 09:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-06 09:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-06 09:00:37 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.022 |  |
| 2026-02-06 09:00:34 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 09:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-06 09:02:46 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-06 09:06:12 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 09:00:34 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 09:10:07 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-06 09:03:02 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 09:03:55 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 09:02:21 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 09:05:51 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 09:02:04 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:03:01 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:06:18 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:09:51 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:07:35 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:02:17 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:25:24 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:06:18 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:03:57 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:07:33 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:05:29 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:05:35 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:13:19 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:01:43 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 09:08:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-06 09:02:20 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-06 09:01:41 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-02-06 09:00:37 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.022 |  |
| 2026-02-06 08:03:16 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-02-06 09:04:41 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.039 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 08:04:30 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.078 |  |
| 2026-02-06 09:04:19 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.112 |  |
| 2026-02-06 09:03:19 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.166 |  |
| 2026-02-06 09:01:04 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.198 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)