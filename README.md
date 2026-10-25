# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_18:14:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,776 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 18:14:31 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-25 18:08:57 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 18:07:27 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-10-25 18:06:27 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 18:06:02 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:04:33 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:04:13 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:04:10 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 18:03:48 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 18:03:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 18:03:33 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-25 18:03:28 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 18:03:27 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-25 18:03:24 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-25 18:03:15 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 18:03:03 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-10-25 18:02:42 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-25 18:02:42 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-25 18:02:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:34 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-10-25 18:02:30 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-25 18:02:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:14 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-25 18:02:05 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:01:42 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-25 18:01:28 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-25 18:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-10-25 18:01:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-25 18:01:06 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-10-25 18:01:05 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-25 18:00:57 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 18:00:52 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 18:00:27 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:00:09 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 18:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-10-25 18:07:27 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-10-25 18:03:03 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-10-25 18:03:48 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-25 18:01:42 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-25 18:02:34 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-10-25 18:01:28 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 18:03:24 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-25 18:02:42 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-25 18:01:05 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-25 18:04:10 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 18:03:15 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 18:02:14 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-25 18:03:27 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-25 18:02:30 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-25 18:08:57 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 18:00:57 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 18:03:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 18:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 18:00:52 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 18:00:09 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 18:03:28 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 18:14:31 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-25 18:02:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:04:13 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:06:02 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:05 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:06:27 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:00:27 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:03:33 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:04:33 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:42 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-25 18:02:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-25 18:01:06 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-10-25 18:01:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)