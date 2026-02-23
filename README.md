# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_22:15:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 22:15:11 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-02-23 22:09:46 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:07:40 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-02-23 22:06:26 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:06:01 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 22:05:31 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:05:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:05:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.132 |  |
| 2026-02-23 22:05:05 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.033 |  |
| 2026-02-23 22:04:02 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:03:51 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:03:51 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:03:48 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:03:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:03:44 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.018 |  |
| 2026-02-23 22:03:23 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:03:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-23 22:03:15 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.063 |  |
| 2026-02-23 22:03:05 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:03:03 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-02-23 22:02:46 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:02:42 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-02-23 22:02:28 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:02:27 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.072 |  |
| 2026-02-23 22:02:09 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:54 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.035 |  |
| 2026-02-23 22:01:53 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-02-23 22:01:49 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:41 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:30 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:22 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:01:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-02-23 22:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.089 |  |
| 2026-02-23 22:01:00 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-23 22:00:31 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-23 21:44:20 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 22:01:53 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-02-23 22:15:11 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-02-23 22:01:00 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-23 22:06:01 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 22:02:46 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:05:31 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:49 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:02:28 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:41 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:03:23 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:05:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:06:26 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:04:02 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:03:51 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:09:46 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:01:30 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 22:02:09 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 21:11:34 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-02-23 22:03:05 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:03:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:03:48 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:01:22 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:00:31 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-23 22:03:44 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.018 |  |
| 2026-02-23 22:07:40 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-02-23 22:03:03 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-02-23 22:03:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-23 22:02:42 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-02-23 22:05:05 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.033 |  |
| 2026-02-23 22:01:54 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.035 |  |
| 2026-02-23 22:01:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-02-23 22:03:15 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.063 |  |
| 2026-02-23 22:02:27 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.072 |  |
| 2026-02-23 22:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.089 |  |
| 2026-02-23 22:05:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)