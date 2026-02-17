# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_16:16:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 16:16:37 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:12:00 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-17 16:11:15 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:10:41 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.579 |  |
| 2026-02-17 16:10:20 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:10:07 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:09:05 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:08:42 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-17 16:08:38 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.044 |  |
| 2026-02-17 16:08:17 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:08:11 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:07:41 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:07:02 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.117 |  |
| 2026-02-17 16:06:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 16:04:57 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:04:46 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 16:04:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:04:08 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 16:04:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:57 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:57 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:29 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-17 16:03:23 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:09 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:50 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:02:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:42 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:34 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 16:02:28 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 16:02:24 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:18 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:18 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-02-17 16:02:10 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:09 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 16:01:57 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:01:45 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:01:28 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 16:08:42 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-17 16:12:00 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-17 16:04:08 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 16:02:09 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 16:02:34 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 16:04:46 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 16:02:28 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 16:06:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 16:03:29 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-17 16:02:24 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:57 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:04:57 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:01:45 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:57 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:11:15 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:07:02 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:23 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:42 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:03:09 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:10 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:01:28 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:16:37 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:10:07 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:08:17 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:10:20 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:01:57 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:04:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:18 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-02-17 16:04:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:07:41 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:02:50 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:08:11 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-17 16:02:18 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-02-17 16:08:38 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.044 |  |
| 2026-02-17 16:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.117 |  |
| 2026-02-17 16:10:41 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.579 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)