# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_07:20:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 07:20:43 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.070 |  |
| 2026-04-16 07:15:13 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:14:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 07:13:29 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-16 07:11:47 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-16 07:10:10 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.290 |  |
| 2026-04-16 07:09:59 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-16 07:08:05 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.045 |  |
| 2026-04-16 07:07:22 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-16 07:07:13 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:06:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-16 07:06:50 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:05:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.118 |  |
| 2026-04-16 07:05:00 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-16 07:04:52 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-04-16 07:04:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 07:04:40 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:04:38 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:04:19 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-16 07:03:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:03:49 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-16 07:03:36 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-04-16 07:02:59 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.161 |  |
| 2026-04-16 07:02:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:02:46 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-04-16 07:02:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-16 07:02:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:02:22 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:02:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-04-16 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.025 |  |
| 2026-04-16 07:02:11 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-16 07:01:55 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-04-16 07:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:01:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:01:28 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 07:01:27 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.035 |  |
| 2026-04-16 07:01:26 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.050 |  |
| 2026-04-16 07:01:12 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-16 07:00:57 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-16 06:33:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 07:03:36 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-04-16 07:07:22 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-16 07:04:19 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-16 07:02:11 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-16 07:13:29 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-16 07:01:12 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-16 07:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-16 07:14:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 07:01:28 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 07:06:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-16 07:11:47 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-16 07:04:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 07:02:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:02:22 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:15:13 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:02:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:03:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:04:38 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:01:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:04:40 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:07:13 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:06:50 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-16 07:09:59 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-16 07:02:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-16 07:05:00 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-16 07:02:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-04-16 07:03:49 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-16 07:01:55 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-04-16 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.025 |  |
| 2026-04-16 07:04:52 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-04-16 07:01:27 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.035 |  |
| 2026-04-16 07:08:05 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.045 |  |
| 2026-04-16 07:02:46 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-04-16 07:01:26 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.050 |  |
| 2026-04-16 07:20:43 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.070 |  |
| 2026-04-16 07:05:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.118 |  |
| 2026-04-16 07:02:59 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.161 |  |
| 2026-04-16 07:10:10 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.290 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)