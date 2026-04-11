# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_14:30:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 14:30:42 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:18:25 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.017 |  |
| 2026-04-11 14:14:32 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:48 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:43 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:08 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:01 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:06:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:05:19 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.128 |  |
| 2026-04-11 14:05:16 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:05:03 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-04-11 14:04:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:04:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:04:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:04:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:03:59 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:03:49 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:03:47 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.069 |  |
| 2026-04-11 14:03:41 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 14:03:40 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:03:26 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-11 14:03:04 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:38 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:02:37 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:31 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:30 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.107 |  |
| 2026-04-11 14:02:19 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:02:06 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:03 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:01:50 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:01:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-11 14:01:33 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.012 |  |
| 2026-04-11 14:01:33 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 14:01:08 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 14:00:44 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-04-11 14:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:00:31 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 14:01:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-11 14:01:33 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 14:01:08 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 14:03:41 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 14:04:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:14:32 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:37 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:04:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:06 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:06:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:48 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:05:16 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:03:04 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:03:40 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:01 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:04:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:00:31 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:03 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:04:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:19 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:08 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:03:59 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:08:43 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:30:42 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:31 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-11 14:02:38 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:03:49 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:01:50 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-11 14:01:33 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.012 |  |
| 2026-04-11 14:18:25 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.017 |  |
| 2026-04-11 14:03:26 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-11 14:00:44 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-04-11 13:20:09 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-04-11 14:05:03 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-04-11 14:03:47 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.069 |  |
| 2026-04-11 14:02:30 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.107 |  |
| 2026-04-11 14:05:19 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)