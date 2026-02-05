# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_00:42:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 00:42:46 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:28:53 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:20:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:09:18 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-06 00:07:37 | Padiyathalawa (Maduru Oya) | 1.69 | 🟢 Normal | -126.000 |  |
| 2026-02-06 00:07:37 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.038 |  |
| 2026-02-06 00:07:35 | Padiyathalawa (Maduru Oya) | 1.76 | 🟢 Normal | -126.000 |  |
| 2026-02-06 00:05:45 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:05:26 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:05:13 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.032 |  |
| 2026-02-06 00:05:00 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -1.333 |  |
| 2026-02-06 00:04:48 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-02-06 00:04:22 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:22 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-06 00:04:22 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:06 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -1.333 |  |
| 2026-02-06 00:03:58 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:03:38 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 00:03:11 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:58 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:54 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:51 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:14 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:02 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:01:49 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-02-06 00:01:46 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.070 |  |
| 2026-02-06 00:01:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 23:13:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 00:01:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 00:09:18 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-06 00:01:42 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 00:03:38 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 00:00:14 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:42:46 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:22 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:01:37 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:28:53 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:58 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:05:45 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:22 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:20:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:02 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:03:11 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 23:03:15 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:05:26 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:51 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:54 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:02:14 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:03:58 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:48 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-02-06 00:04:22 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-06 00:01:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-06 00:01:49 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-02-06 00:05:13 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.032 |  |
| 2026-02-06 00:07:37 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.038 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 00:01:46 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.070 |  |
| 2026-02-05 23:33:18 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.081 |  |
| 2026-02-06 00:05:00 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -1.333 |  |
| 2026-02-06 00:07:37 | Padiyathalawa (Maduru Oya) | 1.69 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)