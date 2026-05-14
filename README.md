# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_03:11:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 03:11:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.090 |  |
| 2026-05-15 03:09:16 | Moragaswewa (Deduru Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:07:37 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.092 |  |
| 2026-05-15 03:07:35 | Moragaswewa (Deduru Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2026-05-15 03:07:10 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 03:07:01 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.026 |  |
| 2026-05-15 03:06:18 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.064 |  |
| 2026-05-15 03:05:27 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 03:04:45 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-05-15 03:04:43 | Badalgama (Maha Oya) | 4.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-15 03:04:28 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 03:04:21 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-15 03:03:46 | Dunamale (Aththanagalu Oya) | 4.58 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 03:03:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-05-15 03:03:34 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:03:24 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.097 |  |
| 2026-05-15 03:03:21 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-05-15 03:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-05-15 03:03:10 | Giriulla (Maha Oya) | 3.87 | 🟢 Normal | -0.029 |  |
| 2026-05-15 03:03:04 | Glencourse (Kelani Ganga) | 14.15 | 🟢 Normal | -0.045 |  |
| 2026-05-15 03:02:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:02:51 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-05-15 03:02:49 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:02:23 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:02:18 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:02:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-05-15 03:01:49 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 03:01:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-05-15 03:01:13 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:00:16 | Magura (Kalu Ganga) | 4.91 | 🟡 Alert | -0.021 |  |
| 2026-05-15 03:00:14 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.040 |  |
| 2026-05-15 02:35:31 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-05-15 02:28:20 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.018 |  |
| 2026-05-15 02:20:02 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 03:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2026-05-15 03:03:46 | Dunamale (Aththanagalu Oya) | 4.58 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 03:00:16 | Magura (Kalu Ganga) | 4.91 | 🟡 Alert | -0.021 |  |
| 2026-05-15 02:03:37 | Hanwella (Kelani Ganga) | 5.98 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-15 02:01:38 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-15 03:04:43 | Badalgama (Maha Oya) | 4.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-15 03:01:49 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 03:05:27 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 03:07:10 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 03:04:28 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:09:16 | Moragaswewa (Deduru Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:02:18 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:02:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:03:34 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:01:13 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 02:03:15 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:02:49 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:02:23 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-15 01:05:53 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2026-05-15 03:03:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-05-15 03:01:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-05-15 03:04:21 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-15 02:05:31 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.020 |  |
| 2026-05-15 03:04:45 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-05-15 03:02:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-05-15 03:03:21 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-05-15 03:07:01 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.026 |  |
| 2026-05-15 03:03:10 | Giriulla (Maha Oya) | 3.87 | 🟢 Normal | -0.029 |  |
| 2026-05-15 03:02:51 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-05-15 03:00:14 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.040 |  |
| 2026-05-15 03:03:04 | Glencourse (Kelani Ganga) | 14.15 | 🟢 Normal | -0.045 |  |
| 2026-05-15 03:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-05-15 03:06:18 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.064 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-15 03:11:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.090 |  |
| 2026-05-15 03:07:37 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.092 |  |
| 2026-05-15 03:03:24 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)