# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_13:40:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,733 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 13:40:09 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:22:29 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:12:26 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:10:50 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-05-30 13:07:59 | Magura (Kalu Ganga) | 2.87 | 🟢 Normal | -0.049 |  |
| 2026-05-30 13:07:00 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:06:48 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:06:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-05-30 13:05:50 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.030 |  |
| 2026-05-30 13:05:37 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.39 | 🟡 Alert | -0.021 |  |
| 2026-05-30 13:05:16 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.081 |  |
| 2026-05-30 13:05:09 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.065 |  |
| 2026-05-30 13:05:08 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:05:02 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-30 13:04:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-30 13:04:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:57 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 13:03:45 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:40 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 13:03:32 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:29 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 13:03:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:57 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-30 13:02:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-05-30 13:02:32 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:29 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-30 13:02:22 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:20 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-05-30 13:02:19 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:01:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-30 13:01:43 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:01:28 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 13:01:13 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | -0.030 |  |
| 2026-05-30 13:01:00 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | -0.087 |  |
| 2026-05-30 13:00:59 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:00:08 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 13:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.39 | 🟡 Alert | -0.021 |  |
| 2026-05-30 13:04:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-30 13:02:29 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-30 13:05:02 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-30 13:03:57 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 13:01:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-30 13:03:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 13:07:00 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:32 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:05:08 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:05:37 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:40:09 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:32 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:02:20 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:12:26 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:29 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:04:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:22:29 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:03:45 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:06:48 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:19 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:00:59 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:05:22 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:22 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:01:43 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:10:50 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-05-30 13:03:40 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 13:01:28 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 13:02:20 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-05-30 13:02:57 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-30 13:00:08 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.022 |  |
| 2026-05-30 13:05:50 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.030 |  |
| 2026-05-30 13:02:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-05-30 13:01:13 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | -0.030 |  |
| 2026-05-30 13:07:59 | Magura (Kalu Ganga) | 2.87 | 🟢 Normal | -0.049 |  |
| 2026-05-30 13:06:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-05-30 13:05:09 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.065 |  |
| 2026-05-30 13:05:16 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.081 |  |
| 2026-05-30 13:01:00 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)