# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_05:15:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,387 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 05:15:23 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:14:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -3.492 |  |
| 2026-01-11 05:11:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:11:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:10:16 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:10:10 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-01-11 05:09:09 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.020 |  |
| 2026-01-11 05:08:30 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-01-11 05:08:19 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:07:38 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.012 |  |
| 2026-01-11 05:07:22 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.102 |  |
| 2026-01-11 05:06:44 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:06:30 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:06:21 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-01-11 05:05:59 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:05:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-11 05:05:17 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 05:04:32 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-01-11 05:04:27 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 05:04:24 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 05:04:10 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-11 05:02:49 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:02:17 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-11 05:02:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.099 |  |
| 2026-01-11 05:01:58 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-01-11 05:01:36 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 05:01:23 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-11 05:01:13 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.014 |  |
| 2026-01-11 05:01:08 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:00:57 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-01-11 05:00:35 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | -3.492 |  |
| 2026-01-11 04:58:57 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:55:04 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:41:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 05:04:10 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-11 05:02:17 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-11 04:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-11 05:05:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-11 05:05:17 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 05:04:27 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 04:05:38 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 05:04:24 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 05:01:36 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 05:11:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:58:57 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:01:08 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:08:19 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:06:44 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:04:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:02:49 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:05:59 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:55:04 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:15:23 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:11:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:10:10 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-01-11 05:08:30 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-01-11 05:04:32 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-01-11 05:01:23 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-11 04:02:02 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.012 |  |
| 2026-01-11 05:07:38 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.012 |  |
| 2026-01-11 05:00:57 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-01-11 05:01:13 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.014 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 05:01:58 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-01-11 05:06:21 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-01-11 05:09:09 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.020 |  |
| 2026-01-11 04:09:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-01-11 04:00:25 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.035 |  |
| 2026-01-11 05:02:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.099 |  |
| 2026-01-11 05:07:22 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.102 |  |
| 2026-01-11 05:14:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -3.492 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)