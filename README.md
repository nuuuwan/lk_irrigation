# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_08:05:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 08:05:41 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-30 08:05:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:03:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:03:48 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:03:33 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-10-30 08:03:22 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.033 |  |
| 2026-10-30 08:03:18 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:03:13 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-30 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.163 |  |
| 2026-10-30 08:03:04 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:03:02 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-30 08:02:59 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:54 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:02:36 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:34 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.063 |  |
| 2026-10-30 08:02:33 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-10-30 08:02:27 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-10-30 08:02:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:02:23 | Ellagawa (Kalu Ganga) | 9.08 | 🟢 Normal | -0.076 |  |
| 2026-10-30 08:02:16 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:14 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-10-30 08:02:06 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-10-30 08:01:58 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 08:01:53 | Putupaula (Kalu Ganga) | 3.45 | 🟡 Alert | -0.010 |  |
| 2026-10-30 08:01:43 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:01:12 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:00:56 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-10-30 08:00:20 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:00:08 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-30 07:23:38 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.081 |  |
| 2026-10-30 07:23:07 | Ellagawa (Kalu Ganga) | 9.13 | 🟢 Normal | -0.076 |  |
| 2026-10-30 07:23:04 | Ellagawa (Kalu Ganga) | 9.13 | 🟢 Normal | -0.076 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 07:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 07:08:19 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-30 08:01:53 | Putupaula (Kalu Ganga) | 3.45 | 🟡 Alert | -0.010 |  |
| 2026-10-30 07:04:18 | Panadugama (Nilwala Ganga) | 5.60 | 🟡 Alert | -0.032 |  |
| 2026-10-30 07:01:05 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.033 |  |
| 2026-10-30 08:00:08 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-30 08:01:58 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 07:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:03:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:36 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:15:46 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:03:04 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:01:43 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:16 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:59 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:00:20 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:03:48 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:01:12 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:05:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:02:54 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:03:18 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:02:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:00:56 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-10-30 08:03:13 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-30 08:03:33 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-10-30 08:02:27 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-10-30 08:02:14 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-10-30 08:05:41 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-30 08:03:02 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-30 07:06:09 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-10-30 07:05:27 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-10-30 08:03:22 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.033 |  |
| 2026-10-30 08:02:33 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-10-30 08:02:06 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-10-30 08:02:34 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.063 |  |
| 2026-10-30 07:10:14 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.070 |  |
| 2026-10-30 08:02:23 | Ellagawa (Kalu Ganga) | 9.08 | 🟢 Normal | -0.076 |  |
| 2026-10-30 07:23:38 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.081 |  |
| 2026-10-30 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)