# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_12:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 12:11:29 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:09:51 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.015 |  |
| 2026-06-08 12:09:02 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:08:15 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 12:08:07 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.038 |  |
| 2026-06-08 12:07:46 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:07:02 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:06:41 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:06:21 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.059 |  |
| 2026-06-08 12:05:48 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-06-08 12:04:20 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:04:07 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:54 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-06-08 12:03:45 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:26 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.042 |  |
| 2026-06-08 12:03:18 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.060 |  |
| 2026-06-08 12:03:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:12 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:04 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-06-08 12:02:51 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 12:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-08 12:02:47 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 12:02:43 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-08 12:02:25 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:02:23 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-06-08 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -0.020 |  |
| 2026-06-08 12:02:07 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:02:00 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:55 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.031 |  |
| 2026-06-08 12:01:52 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 12:01:41 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-08 12:01:34 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:28 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.060 |  |
| 2026-06-08 12:01:11 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-06-08 12:01:08 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:00:38 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-06-08 12:00:25 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 12:02:43 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-08 12:02:47 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 12:08:15 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 12:02:51 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 12:01:52 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 12:01:11 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:34 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:08 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:04:20 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:01:41 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:02:25 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:45 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:06:41 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:09:02 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:11:29 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:04:07 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:02:00 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:07:02 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:02:07 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:07:46 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:00:25 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:03:12 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-08 12:02:23 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-06-08 12:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-08 12:00:38 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-06-08 12:09:51 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.015 |  |
| 2026-06-08 12:03:04 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-06-08 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -0.020 |  |
| 2026-06-08 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-06-08 12:03:54 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-06-08 12:05:48 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-06-08 12:01:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-08 12:01:55 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.031 |  |
| 2026-06-08 12:08:07 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.038 |  |
| 2026-06-08 12:03:26 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.042 |  |
| 2026-06-08 12:06:21 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.059 |  |
| 2026-06-08 12:01:28 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.060 |  |
| 2026-06-08 12:03:18 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)