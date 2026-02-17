# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_06:20:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 06:20:41 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.016 |  |
| 2026-02-17 06:18:48 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.016 |  |
| 2026-02-17 06:12:54 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-02-17 06:07:32 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:07:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:06:51 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:06:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.183 |  |
| 2026-02-17 06:06:09 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.075 |  |
| 2026-02-17 06:05:46 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:05:41 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-17 06:05:39 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:04:37 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:04:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-02-17 06:04:29 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 06:04:21 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -6.760 |  |
| 2026-02-17 06:04:13 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-17 06:03:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-17 06:03:41 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 06:03:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-17 06:03:22 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:03:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-02-17 06:03:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:02:34 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.029 |  |
| 2026-02-17 06:02:20 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:02:19 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:02:15 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-17 06:01:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:52 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:34 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-02-17 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.047 |  |
| 2026-02-17 06:00:52 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-17 06:00:32 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -6.760 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 06:04:13 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-17 06:05:41 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-17 06:02:15 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-17 06:04:29 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 06:03:41 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 06:03:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-17 06:01:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:07:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:05:39 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:03:22 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:03:59 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:04:37 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:05:06 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:02:20 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:03:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:02:19 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:07:32 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:05:46 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:06:51 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:52 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:01:36 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:15:43 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:01:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:04:49 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 06:03:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-17 06:00:52 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-17 06:01:34 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-02-17 06:12:54 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-02-17 06:04:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-02-17 06:18:48 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.016 |  |
| 2026-02-17 06:20:41 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.016 |  |
| 2026-02-17 06:02:34 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.029 |  |
| 2026-02-17 06:03:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-02-17 06:01:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.047 |  |
| 2026-02-17 06:06:09 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.075 |  |
| 2026-02-17 06:06:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.183 |  |
| 2026-02-17 06:04:21 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -6.760 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)