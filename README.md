# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_08:05:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 08:05:51 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:38 | Dunamale (Aththanagalu Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:09 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 08:04:39 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-14 08:04:20 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.030 |  |
| 2026-02-14 08:04:13 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-02-14 08:03:52 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:03:48 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:03:32 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:03:28 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:03:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-14 08:03:25 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-02-14 08:03:12 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:02:56 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-14 08:02:53 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:02:33 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.099 |  |
| 2026-02-14 08:02:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:02:06 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:01:48 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:01:27 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:00:44 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 08:00:35 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:00:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:00:27 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:00:16 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.048 |  |
| 2026-02-14 08:00:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 07:22:34 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.048 |  |
| 2026-02-14 07:16:15 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 07:12:10 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.048 |  |
| 2026-02-14 07:11:42 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 07:04:39 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-02-14 08:03:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-14 08:02:56 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-14 08:00:44 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 08:05:09 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 08:00:27 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:02:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:00:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:01:48 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:02:53 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:01:27 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 07:16:15 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 07:04:32 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:03:48 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:00:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:02:33 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:38 | Dunamale (Aththanagalu Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:03:32 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:05:51 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:00:35 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 08:03:52 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 07:05:04 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:03:28 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:02:06 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-14 08:03:12 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-14 07:02:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.012 |  |
| 2026-02-14 08:04:39 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-14 08:03:25 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-02-14 07:08:58 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-02-14 07:05:44 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-02-14 08:04:20 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.030 |  |
| 2026-02-14 07:06:42 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.031 |  |
| 2026-02-14 08:04:13 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-02-14 08:00:16 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.048 |  |
| 2026-02-14 08:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.099 |  |
| 2026-02-14 07:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)