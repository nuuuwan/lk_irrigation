# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_09:14:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 09:14:38 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:11:57 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.054 |  |
| 2026-01-15 09:11:26 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.049 |  |
| 2026-01-15 09:07:39 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:07:09 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.138 |  |
| 2026-01-15 09:06:15 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:06:06 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:05:57 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:05:55 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.019 |  |
| 2026-01-15 09:04:47 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:04:42 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-01-15 09:04:07 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:04:03 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:59 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.085 |  |
| 2026-01-15 09:03:38 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:03:30 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:29 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:27 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:03:06 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-01-15 09:03:01 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:01 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:02:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:02:43 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-01-15 09:02:40 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:02:39 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:02:28 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.210 |  |
| 2026-01-15 09:02:18 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-15 09:02:11 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-01-15 09:01:42 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:01:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:01:07 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:03 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:00:40 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:00:27 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:59:23 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.265 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 08:59:23 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-01-15 09:03:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:04:47 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:06:15 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:01 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:29 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:05:57 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:30 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:07:39 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:01:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:04:03 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:02:39 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:06:06 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:04:07 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:59 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:02:40 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:14:38 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:01 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 09:03:27 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:42 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:00:27 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:00:40 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:03 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:01:07 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:03:38 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-15 09:05:55 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.019 |  |
| 2026-01-15 09:02:43 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-01-15 09:04:42 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-01-15 09:02:18 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-15 09:03:06 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-01-15 09:11:26 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.049 |  |
| 2026-01-15 09:11:57 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.054 |  |
| 2026-01-15 09:02:11 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-01-15 09:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.085 |  |
| 2026-01-15 09:07:09 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.138 |  |
| 2026-01-15 09:02:28 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)