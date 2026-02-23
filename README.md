# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_02:11:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,387 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 02:11:13 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-02-24 02:10:14 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:08:46 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-24 02:08:17 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:07:58 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-24 02:06:24 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -2.250 |  |
| 2026-02-24 02:06:08 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -2.250 |  |
| 2026-02-24 02:06:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-24 02:05:34 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-24 02:04:46 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-02-24 02:03:53 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-02-24 02:03:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:03:49 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:03:43 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.266 |  |
| 2026-02-24 02:03:15 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 02:03:14 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:03:08 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:02:42 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:02:32 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-02-24 02:02:31 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-24 02:02:31 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.036 |  |
| 2026-02-24 02:02:29 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.121 |  |
| 2026-02-24 02:02:28 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:02:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:55 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.085 |  |
| 2026-02-24 02:01:53 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:53 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:39 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:02 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:00:56 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 02:00:54 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:42:30 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:29:04 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 02:06:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-24 02:02:31 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-24 02:05:34 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-24 01:01:17 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-24 02:03:15 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 02:03:08 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:52 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:03:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:53 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:00:54 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:53 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:03:49 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:03:30 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:01:39 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:08:17 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:02:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:03:14 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:04:43 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:02:28 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:10:14 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:02:42 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 02:08:46 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-24 02:07:58 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-24 02:02:32 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-02-24 02:00:56 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 02:03:53 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-02-24 02:04:46 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-24 02:02:31 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.036 |  |
| 2026-02-24 00:11:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-02-24 02:11:13 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-02-24 01:08:26 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.053 |  |
| 2026-02-24 02:01:55 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.085 |  |
| 2026-02-24 02:02:29 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.121 |  |
| 2026-02-24 02:03:43 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.266 |  |
| 2026-02-24 02:06:24 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)