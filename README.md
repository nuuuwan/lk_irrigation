# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_01:42:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,676 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 01:42:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-30 01:33:17 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:20:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-30 01:16:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:15:27 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.017 |  |
| 2026-04-30 01:12:21 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:10:29 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-30 01:09:59 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:09:32 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-04-30 01:08:47 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:08:16 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-04-30 01:07:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-30 01:06:45 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-30 01:06:09 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 01:04:45 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:04:25 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:04:17 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.035 |  |
| 2026-04-30 01:03:56 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.100 |  |
| 2026-04-30 01:03:44 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-30 01:03:07 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:02:53 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:02:50 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-30 01:02:41 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.131 |  |
| 2026-04-30 01:02:09 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-04-30 01:02:01 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:01:54 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.200 |  |
| 2026-04-30 01:01:51 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:01:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:01:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:00:20 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-30 01:00:18 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 01:20:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-30 01:00:20 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-30 01:06:09 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 00:05:24 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 01:10:29 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-30 01:06:45 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 01:42:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-30 01:16:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:01:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:09:59 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:03:07 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:01:51 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:04:45 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:11:47 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:01:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:02:01 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:33:17 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:04:25 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:02:53 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:12:21 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:09:32 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-04-30 01:03:44 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-30 01:02:50 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-30 01:08:16 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-04-30 01:15:27 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.017 |  |
| 2026-04-30 01:02:09 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-04-30 01:04:17 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.035 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 00:05:07 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-04-30 01:07:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-30 01:00:18 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.066 |  |
| 2026-04-30 01:03:56 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.100 |  |
| 2026-04-30 01:02:41 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.131 |  |
| 2026-04-30 01:01:54 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)