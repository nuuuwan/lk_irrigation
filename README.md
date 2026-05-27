# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_20:11:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,321 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 20:11:59 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:11:12 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-05-27 20:10:30 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:10:03 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-27 20:09:37 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-27 20:09:32 | Hanwella (Kelani Ganga) | 4.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 20:07:00 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:06:55 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-27 20:05:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-05-27 20:05:53 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:05:38 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 20:04:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-27 20:04:44 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:04:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-27 20:04:27 | Rathnapura (Kalu Ganga) | 4.48 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-05-27 20:04:13 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-05-27 20:03:56 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:03:54 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 20:03:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:03:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:02:33 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-27 20:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:02:20 | Deraniyagala (Kelani Ganga) | 3.05 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-27 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 20:02:12 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:02:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-27 20:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-27 20:01:22 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-27 20:01:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:01:16 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-27 20:01:08 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:00:32 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-05-27 20:00:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:00:11 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:55:48 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 20:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-27 20:00:32 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-05-27 20:04:27 | Rathnapura (Kalu Ganga) | 4.48 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-05-27 20:11:12 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-05-27 20:02:20 | Deraniyagala (Kelani Ganga) | 3.05 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-27 20:09:37 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-27 20:01:22 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-27 20:02:33 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-27 20:10:03 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-27 20:04:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-27 20:06:55 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-27 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 20:03:54 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 20:09:32 | Hanwella (Kelani Ganga) | 4.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 20:05:38 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 20:01:08 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:03:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:15:39 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:01:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:00:11 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:03:56 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:00:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:05:53 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:07:00 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:10:30 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:04:44 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:03:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:11:59 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:02:12 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-27 20:04:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-27 20:02:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-27 20:01:16 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-27 20:05:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-05-27 20:04:13 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.033 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)