# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_08:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,186 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 08:08:17 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 12.522 | 🔺 Rising |
| 2026-06-12 08:08:07 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | -0.191 |  |
| 2026-06-12 08:07:54 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 12.522 | 🔺 Rising |
| 2026-06-12 08:06:14 | Thawalama (Gin Ganga) | 3.75 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-12 08:06:02 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | 0.275 | 🔺 Rising |
| 2026-06-12 08:05:43 | Rathnapura (Kalu Ganga) | 5.98 | 🟡 Alert | -0.023 |  |
| 2026-06-12 08:05:39 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-12 08:04:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:04:27 | Glencourse (Kelani Ganga) | 12.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 08:04:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.196 |  |
| 2026-06-12 08:04:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-12 08:03:56 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-06-12 08:03:45 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-12 08:03:38 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:03:24 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-12 08:03:15 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.055 |  |
| 2026-06-12 08:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-06-12 08:03:04 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.043 |  |
| 2026-06-12 08:02:49 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.109 |  |
| 2026-06-12 08:02:43 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-12 08:02:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:02:35 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 08:02:33 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 08:02:31 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-06-12 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-06-12 08:02:09 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 08:02:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:02:04 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.032 |  |
| 2026-06-12 08:02:03 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 133.333 | 🔺 Rising |
| 2026-06-12 08:01:56 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -72.000 |  |
| 2026-06-12 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -72.000 |  |
| 2026-06-12 08:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:01:36 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 133.333 | 🔺 Rising |
| 2026-06-12 08:01:34 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 08:01:09 | Moraketiya (Walawe Ganga) | 1.53 | 🟢 Normal | -0.066 |  |
| 2026-06-12 08:00:49 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:00:41 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:00:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 08:06:02 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | 0.275 | 🔺 Rising |
| 2026-06-12 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-06-12 08:05:43 | Rathnapura (Kalu Ganga) | 5.98 | 🟡 Alert | -0.023 |  |
| 2026-06-12 08:02:03 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 133.333 | 🔺 Rising |
| 2026-06-12 08:08:17 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 12.522 | 🔺 Rising |
| 2026-06-12 07:03:34 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-12 08:03:24 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-12 08:03:56 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-06-12 08:06:14 | Thawalama (Gin Ganga) | 3.75 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-12 07:08:24 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-12 08:04:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-12 08:05:39 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-12 08:01:34 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 07:15:10 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-12 08:02:43 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-12 08:03:45 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-12 08:04:27 | Glencourse (Kelani Ganga) | 12.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 08:02:09 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 08:02:35 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 08:02:33 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 07:09:45 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 08:00:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:00:41 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:03:38 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:02:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:02:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:00:49 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:04:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 08:02:31 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-06-12 08:02:04 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.032 |  |
| 2026-06-12 08:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-06-12 08:03:04 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.043 |  |
| 2026-06-12 08:03:15 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.055 |  |
| 2026-06-12 08:01:09 | Moraketiya (Walawe Ganga) | 1.53 | 🟢 Normal | -0.066 |  |
| 2026-06-12 08:02:49 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.109 |  |
| 2026-06-12 08:08:07 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | -0.191 |  |
| 2026-06-12 08:04:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.196 |  |
| 2026-06-12 08:01:56 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)