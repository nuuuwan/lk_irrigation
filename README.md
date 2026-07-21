# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_04:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 04:14:53 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:11:56 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.309 |  |
| 2026-07-22 04:09:39 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:09:02 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-22 04:08:18 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:07:29 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:07:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:06:35 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:06:11 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:05:40 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:05:23 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:34 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-22 04:04:25 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:21 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:15 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:11 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:04 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-07-22 04:03:48 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:03:47 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:03:46 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-22 04:03:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-22 04:03:08 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:03:00 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:02:51 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.193 |  |
| 2026-07-22 04:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-07-22 04:02:22 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:02:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-22 04:02:14 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:01:56 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:01:41 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:01:34 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-22 04:01:13 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-22 04:00:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:00:34 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:54:02 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-07-22 03:44:19 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:42:56 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:42:54 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:42:51 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:42:48 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:39:56 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:38:05 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:34:15 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 04:04:04 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-07-22 04:03:46 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-22 04:03:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-22 04:09:02 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-22 04:01:34 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-22 04:02:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-22 04:04:34 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-22 04:00:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:02:22 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:05:30 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:03:08 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:01:56 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:14:53 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:06:11 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:03:00 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:05:23 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:05:40 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:02:52 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:07:29 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:01:41 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:00:34 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:08:18 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:03:48 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:07:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:11 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:02:14 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:09:39 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:00 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:04:25 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:06:35 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-22 03:42:56 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:01:13 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-22 04:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-22 02:05:43 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-07-21 18:04:58 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-07-22 04:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-07-22 04:02:51 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.193 |  |
| 2026-07-22 04:11:56 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.309 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)