# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_22:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 22:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.016 |  |
| 2026-02-24 22:16:31 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:12:57 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.017 |  |
| 2026-02-24 22:09:15 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-24 22:08:07 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:07:49 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-24 22:07:45 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:07:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-24 22:07:33 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:07:20 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-02-24 22:05:55 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:05:52 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:05:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-24 22:05:05 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:04:41 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-02-24 22:04:31 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:04:17 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:58 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:47 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 22:02:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:16 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:15 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:10 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:09 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:08 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-02-24 22:02:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.079 |  |
| 2026-02-24 22:02:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:01:48 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-02-24 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:00:54 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:00:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:00:46 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:00:23 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 21:27:47 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 22:05:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-24 22:07:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-24 22:09:15 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-24 22:02:47 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 22:04:31 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:00:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:01:48 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:00:46 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:16:31 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:16 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:10 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 21:05:07 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:05:52 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:02:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:08:07 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:00:23 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:05:55 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:05:05 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:07:20 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-02-24 22:07:49 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-24 22:04:17 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:58 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:00:54 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:09 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:02:15 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-24 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-24 21:27:47 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.015 |  |
| 2026-02-24 22:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.016 |  |
| 2026-02-24 22:12:57 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.017 |  |
| 2026-02-24 22:04:41 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-02-24 21:02:41 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-02-24 22:02:08 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 21:03:41 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-24 22:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-02-24 22:02:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)