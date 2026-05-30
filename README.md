# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_07:38:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,499 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 07:38:10 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:38:01 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.046 |  |
| 2026-05-30 07:29:17 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:26:21 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:16:34 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:13:13 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-05-30 07:12:55 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | -0.037 |  |
| 2026-05-30 07:12:09 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.076 |  |
| 2026-05-30 07:11:47 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-05-30 07:10:58 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:10:40 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-30 07:09:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:08:54 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:08:53 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:08:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:07:33 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-30 07:07:33 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:06:53 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.037 |  |
| 2026-05-30 07:06:22 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-05-30 07:06:15 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.028 |  |
| 2026-05-30 07:05:49 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:05:07 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:05:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.035 |  |
| 2026-05-30 07:04:38 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.037 |  |
| 2026-05-30 07:04:11 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:04:06 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:03:35 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.003 |  |
| 2026-05-30 07:03:28 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:03:12 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2026-05-30 07:03:09 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-30 07:02:39 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:02:17 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.041 |  |
| 2026-05-30 07:01:41 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:01:41 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:01:39 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-30 07:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.062 |  |
| 2026-05-30 07:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-30 07:00:59 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:00:33 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.040 |  |
| 2026-05-30 07:00:15 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 07:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.062 |  |
| 2026-05-30 07:10:40 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-30 07:01:39 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-30 07:03:35 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.003 |  |
| 2026-05-30 07:04:06 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:01:41 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:08:54 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:26:21 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:08:53 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:02:39 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:04:11 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:05:07 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:16:34 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:38:10 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:09:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:08:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:03:28 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:10:58 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:29:17 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:01:41 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:07:33 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 07:13:13 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-05-30 07:11:47 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-05-30 07:06:22 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-05-30 07:07:33 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-30 07:03:09 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-30 07:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-30 07:00:15 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-05-30 07:06:15 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.028 |  |
| 2026-05-30 07:05:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.035 |  |
| 2026-05-30 07:12:55 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | -0.037 |  |
| 2026-05-30 07:06:53 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.037 |  |
| 2026-05-30 07:04:38 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.037 |  |
| 2026-05-30 07:00:33 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.040 |  |
| 2026-05-30 07:02:17 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.041 |  |
| 2026-05-30 07:38:01 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.046 |  |
| 2026-05-30 07:03:12 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2026-05-30 07:12:09 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.076 |  |
| 2026-05-30 06:04:25 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)