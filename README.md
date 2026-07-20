# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_08:06:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,153 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 08:06:46 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 08:05:52 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-20 08:04:58 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-20 08:04:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:04:03 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-07-20 08:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:47 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.083 |  |
| 2026-07-20 08:03:40 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.042 |  |
| 2026-07-20 08:03:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:28 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-07-20 08:03:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:23 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:17 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-20 08:03:16 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:07 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.012 |  |
| 2026-07-20 08:03:03 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:25 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:16 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:10 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:01:44 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:00:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-20 08:00:47 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-20 07:27:07 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-20 07:25:48 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.007 |  |
| 2026-07-20 07:22:46 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.003 |  |
| 2026-07-20 07:19:15 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 08:03:28 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-07-20 08:03:17 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-20 08:04:58 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-20 08:06:46 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 07:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 06:00:43 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-20 08:05:52 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-20 07:10:20 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 07:10:09 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-20 07:22:46 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.003 |  |
| 2026-07-20 08:03:23 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:03:34 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:01:44 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:47 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:04:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:10:18 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:16 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:04:26 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:03 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:25 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:03:13 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:16 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:02:10 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:25:48 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.007 |  |
| 2026-07-20 07:16:28 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-07-20 08:00:47 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-20 08:00:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-20 08:03:07 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.012 |  |
| 2026-07-20 08:03:40 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.042 |  |
| 2026-07-20 07:06:45 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.053 |  |
| 2026-07-20 08:04:03 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-07-20 07:05:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.065 |  |
| 2026-07-20 08:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.083 |  |
| 2026-07-20 07:04:02 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)