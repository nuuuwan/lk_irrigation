# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_04:30:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 04:30:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:25:36 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 04:21:33 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:21:27 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.082 |  |
| 2026-06-29 04:12:42 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-29 04:09:51 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-29 04:09:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.045 |  |
| 2026-06-29 04:08:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.082 |  |
| 2026-06-29 04:08:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 04:07:55 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:07:23 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:06:41 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:05:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:04:44 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:04:40 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:04:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.052 |  |
| 2026-06-29 04:04:21 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-29 04:04:03 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:02:56 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.039 |  |
| 2026-06-29 04:02:06 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:53 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 04:01:51 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-29 04:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-06-29 04:01:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:16 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:06 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.013 |  |
| 2026-06-29 04:00:54 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.065 |  |
| 2026-06-29 04:00:47 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:00:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:59:44 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-06-29 04:09:51 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-29 04:01:51 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-29 04:12:42 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-29 04:25:36 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 04:04:21 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-29 03:09:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 04:01:53 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 04:08:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 04:04:03 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:00:47 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:04:40 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 04:07:23 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:04:44 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:16:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:16 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:30:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:01:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:05:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:56 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:21:33 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:07:55 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:06:41 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:06 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 03:03:10 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-29 04:01:06 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.013 |  |
| 2026-06-29 04:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.039 |  |
| 2026-06-29 04:01:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-06-29 04:09:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.045 |  |
| 2026-06-29 04:04:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.052 |  |
| 2026-06-29 04:00:54 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.065 |  |
| 2026-06-29 04:21:27 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.082 |  |
| 2026-06-29 04:08:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)