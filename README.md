# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_07:29:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,779 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 07:29:03 | Kuda Oya (Kirindi Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:24:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.043 |  |
| 2026-05-10 07:13:41 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-05-10 07:13:18 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-05-10 07:11:57 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:10:11 | Katharagama (Menik Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-10 07:09:44 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-10 07:08:28 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.140 |  |
| 2026-05-10 07:08:21 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:08:06 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.018 |  |
| 2026-05-10 07:06:32 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-05-10 07:05:47 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.088 |  |
| 2026-05-10 07:05:43 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | -0.047 |  |
| 2026-05-10 07:04:56 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-10 07:04:20 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.232 |  |
| 2026-05-10 07:03:38 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.029 |  |
| 2026-05-10 07:03:25 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-05-10 07:02:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:02:43 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.096 |  |
| 2026-05-10 07:02:32 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 07:02:31 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-10 07:02:29 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-05-10 07:02:29 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:02:25 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-10 07:02:20 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 07:02:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:02:07 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 07:01:53 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:01:35 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.108 |  |
| 2026-05-10 07:01:30 | Thanthirimale (Malwathu Oya) | 3.09 | 🟢 Normal | -0.012 |  |
| 2026-05-10 07:01:29 | Wellawaya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.147 |  |
| 2026-05-10 07:01:21 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:01:13 | Kuda Oya (Kirindi Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:01:09 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:00:53 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.082 |  |
| 2026-05-10 07:00:37 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:00:30 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.073 |  |
| 2026-05-10 07:00:20 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.037 |  |
| 2026-05-10 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.040 |  |
| 2026-05-10 06:38:29 | Galgamuwa (Mee Oya) | 0.95 | 🟢 Normal | -0.140 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 07:04:56 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-10 07:02:07 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 06:05:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 07:02:20 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 07:02:32 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 07:08:21 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:01:53 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:01:21 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:02:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:01:09 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:00:37 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:02:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:11:57 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:29:03 | Kuda Oya (Kirindi Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 07:13:41 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-05-10 07:13:18 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-05-10 07:10:11 | Katharagama (Menik Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-10 07:02:31 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-10 07:02:25 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-10 07:01:30 | Thanthirimale (Malwathu Oya) | 3.09 | 🟢 Normal | -0.012 |  |
| 2026-05-10 07:08:06 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.018 |  |
| 2026-05-10 07:06:32 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-05-10 07:09:44 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-10 07:03:38 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.029 |  |
| 2026-05-10 06:04:35 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-10 07:03:25 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-05-10 07:02:29 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-05-10 07:00:20 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.037 |  |
| 2026-05-10 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.040 |  |
| 2026-05-10 07:24:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.043 |  |
| 2026-05-10 07:05:43 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | -0.047 |  |
| 2026-05-10 07:00:30 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.073 |  |
| 2026-05-10 07:00:53 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.082 |  |
| 2026-05-10 07:05:47 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.088 |  |
| 2026-05-10 07:02:43 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.096 |  |
| 2026-05-10 07:01:35 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.108 |  |
| 2026-05-10 07:08:28 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.140 |  |
| 2026-05-10 07:01:29 | Wellawaya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.147 |  |
| 2026-05-10 07:04:20 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)