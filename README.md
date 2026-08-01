# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_18:13:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,228 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 18:13:51 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:09:23 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:08:20 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.083 |  |
| 2026-08-01 18:08:07 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:07:18 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:05:51 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.022 |  |
| 2026-08-01 18:05:27 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:05:19 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:05:11 | Rathnapura (Kalu Ganga) | 3.28 | 🟢 Normal | 1.618 | 🔺 Rising |
| 2026-08-01 18:04:55 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:32 | Glencourse (Kelani Ganga) | 13.42 | 🟢 Normal | -0.281 |  |
| 2026-08-01 18:04:27 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:25 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.143 |  |
| 2026-08-01 18:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:02 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-01 18:03:45 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.085 |  |
| 2026-08-01 18:03:42 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | 1.618 | 🔺 Rising |
| 2026-08-01 18:03:23 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.275 |  |
| 2026-08-01 18:02:51 | Hanwella (Kelani Ganga) | 5.53 | 🟢 Normal | -0.071 |  |
| 2026-08-01 18:02:45 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.284 |  |
| 2026-08-01 18:02:41 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:02:33 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:23 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:22 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:02:15 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-01 18:02:12 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:07 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-08-01 18:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:01:41 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.114 |  |
| 2026-08-01 18:01:22 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:01:13 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 18:00:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:00:13 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-08-01 18:00:12 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:00:12 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-01 18:00:11 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 18:05:11 | Rathnapura (Kalu Ganga) | 3.28 | 🟢 Normal | 1.618 | 🔺 Rising |
| 2026-08-01 18:00:12 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-01 18:02:15 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-01 18:03:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-01 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:02:41 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:00:11 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:01:13 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:05:27 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:08:07 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:12 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:01:22 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:02 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:13:51 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:22 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:00:12 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:55 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:33 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:27 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:09:23 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:00:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:05:19 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:02:07 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-08-01 17:22:28 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2026-08-01 18:05:51 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.022 |  |
| 2026-08-01 18:00:13 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-08-01 18:03:23 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 18:02:51 | Hanwella (Kelani Ganga) | 5.53 | 🟢 Normal | -0.071 |  |
| 2026-08-01 18:08:20 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.083 |  |
| 2026-08-01 18:03:45 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.085 |  |
| 2026-08-01 18:01:41 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.114 |  |
| 2026-08-01 18:04:25 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.143 |  |
| 2026-08-01 18:03:08 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.275 |  |
| 2026-08-01 18:04:32 | Glencourse (Kelani Ganga) | 13.42 | 🟢 Normal | -0.281 |  |
| 2026-08-01 18:02:45 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.284 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)