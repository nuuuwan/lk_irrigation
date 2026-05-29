# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_04:47:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,384 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 04:47:47 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:31:35 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.027 |  |
| 2026-05-30 04:10:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.085 |  |
| 2026-05-30 04:10:02 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.071 |  |
| 2026-05-30 04:09:00 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.067 |  |
| 2026-05-30 04:07:14 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-05-30 04:06:56 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.019 |  |
| 2026-05-30 04:06:41 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:06:37 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -1.946 |  |
| 2026-05-30 04:06:26 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.027 |  |
| 2026-05-30 04:06:00 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -1.946 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 03:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-30 04:00:51 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-30 04:03:07 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 04:03:06 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.005 |  |
| 2026-05-30 04:03:24 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:03:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:47:47 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:01:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:03:18 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:02:21 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:08:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:00:20 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:01:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:06:41 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:04:45 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:01:37 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 04:03:48 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.005 |  |
| 2026-05-30 04:04:26 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-05-30 04:03:36 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-30 04:01:11 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-30 04:02:48 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-05-30 04:04:31 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-30 04:07:14 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-05-30 04:06:56 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.019 |  |
| 2026-05-30 04:00:52 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-05-30 04:00:23 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.023 |  |
| 2026-05-30 04:31:35 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.027 |  |
| 2026-05-30 04:06:26 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.027 |  |
| 2026-05-30 04:03:08 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.031 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-30 04:04:13 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.039 |  |
| 2026-05-30 04:01:44 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.043 |  |
| 2026-05-30 04:09:00 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.067 |  |
| 2026-05-30 04:10:02 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.071 |  |
| 2026-05-30 04:10:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.085 |  |
| 2026-05-30 04:01:13 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.098 |  |
| 2026-05-30 04:06:37 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -1.946 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)