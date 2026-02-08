# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_18:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 18:13:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:10:34 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:10:12 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:09:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:08:10 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:08:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:07:46 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:06:28 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:06:06 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:05:44 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:05:18 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:05:05 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:04:10 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 18:04:05 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:03:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:03:30 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-08 18:03:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:45 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:45 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:41 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:02:22 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-08 18:02:04 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-08 18:02:02 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:17 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-02-08 18:01:13 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:10 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.053 |  |
| 2026-02-08 18:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:00:41 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-08 18:00:39 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.063 |  |
| 2026-02-08 18:00:37 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:00:11 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:23:04 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 18:03:30 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-08 18:00:41 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-08 18:04:05 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-08 18:04:10 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 15:04:07 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.003 |  |
| 2026-02-08 18:03:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:00:11 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:13 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:05:18 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:03:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:05:05 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:45 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:06:06 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:01:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:05:44 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:00:37 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:10:12 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:08:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:02 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:13:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:10:34 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:22 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:45 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:08:10 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:09:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:06:28 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:07:46 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:02:41 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:02:04 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-08 18:01:17 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-02-08 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-02-08 18:01:10 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.053 |  |
| 2026-02-08 17:09:24 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.055 |  |
| 2026-02-08 18:00:39 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.063 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)