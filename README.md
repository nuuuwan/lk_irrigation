# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_10:36:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 10:36:12 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:31:49 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.045 |  |
| 2026-01-15 10:22:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:17:42 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.077 |  |
| 2026-01-15 10:15:44 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-15 10:11:54 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:10:17 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-15 10:09:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-01-15 10:08:59 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:07:30 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.039 |  |
| 2026-01-15 10:07:09 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-01-15 10:06:59 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:05:51 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:05:41 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-01-15 10:05:33 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:04:43 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:36 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:22 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:04 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:03:43 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:03:38 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.111 |  |
| 2026-01-15 10:03:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:03:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-15 10:03:10 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-01-15 10:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-01-15 10:03:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:02:50 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:02:30 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-01-15 10:02:26 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:02:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:39 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:36 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:35 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:01:32 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:01:09 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:00:40 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:00:30 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 10:15:44 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-15 10:03:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-15 10:10:17 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-15 10:01:35 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:02:26 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:00:30 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:43 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:04 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:36 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:03:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:01:09 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:08:59 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:22:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:06:59 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:02:50 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:36:12 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:11:54 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:04:22 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:05:51 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:03:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:00:40 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 10:05:33 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:36 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:39 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:01:32 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:03:43 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:02:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:05:41 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-01-15 10:03:10 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-01-15 10:07:09 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-01-15 10:02:30 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-01-15 09:03:06 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-01-15 10:09:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-01-15 10:07:30 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.039 |  |
| 2026-01-15 10:31:49 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.045 |  |
| 2026-01-15 10:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-01-15 10:17:42 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.077 |  |
| 2026-01-15 10:03:38 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)